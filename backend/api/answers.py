# フラッシュ数学暗算の答え合わせを行うAPIエンドポイント
import json
import azure.functions as func
from typing import List

from mock.mock_question import QUESTIONS

answer_blueprint = func.Blueprint()

@answer_blueprint.route(route="answers", methods=["POST"])
def check_answer(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # リクエストボディの取得
        req_body = req.get_json()
    except ValueError:
        return func.HttpResponse(
            body=json.dumps({"error": "Invalid JSON in request body"}),
            mimetype="application/json",
            status_code=400
        )
    answer:str = req_body.get("answer") # ユーザーの答え(合計値)
    question_ids: List[int] = req_body.get("question_ids")

    if answer is None or question_ids is None:
        return func.HttpResponse(
            body=json.dumps({"error": "Missing 'answer' or 'question_ids' in request body"}),
            mimetype="application/json",
            status_code=400
        )
    
    # TODO: QuestionServiceを作ってそこから問題を取得するようにする
    # 問題の取得
    questions = [q for q in QUESTIONS if q["id"] in question_ids]
    # TODO: AnswerServiceを作って採点
    # 分数も含む予定だから難しいかもしれないが実装したい(SymPyを使いたい)

    # とりあえず仮のデータを返す
    result = {
        "correct": True,
        "answers": [q["answer"] for q in questions],
        "expected_answer": "58"
    }

    return func.HttpResponse(
        body=json.dumps(result),
        mimetype="application/json",
        status_code=200
    )