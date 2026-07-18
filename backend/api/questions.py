# フラッシュ数学暗算の問題を返すAPIのエンドポイント
import json
import azure.functions as func


from mock.mock_question import QUESTIONS

questions_blueprint = func.Blueprint()

@questions_blueprint.route(route="questions", methods=["POST"])
def generate_questions(req: func.HttpRequest) -> func.HttpResponse:

    # difficultyとquestion_sizeを取得する
    try:
        req_body = req.get_json()
    except:
        return func.HttpResponse(
            body=json.dumps({"error": "Invalid JSON in request body"}),
            mimetype="application/json",
            status_code=400
        )
    
    difficulty = req_body.get("difficulty")
    question_size = req_body.get("question_size")

    if difficulty is None or question_size is None:
        return func.HttpResponse(
            body=json.dumps({"error": "Missing 'difficulty' or 'question_size' in request body"}),
            mimetype="application/json",
            status_code=400
        )

    # とりあえず、固定の問題を返すようにする
    # TODO: QuestionServiceを作ってそこから問題を取得するようにする
    questions = QUESTIONS[0:3]  # とりあえず、最初の3問だけ返す

    return func.HttpResponse(
        body=json.dumps({
            "questions": [
                {
                    "question_id": q["id"],
                    "question": q["expression"]
                }
                for q in questions
            ],
            "difficulty": difficulty
        }),
        mimetype="application/json",
        status_code=200
    )