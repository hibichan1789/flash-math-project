import azure.functions as func

# ルーティングを書く
blue_print = func.Blueprint()

# 疎通確認のヘルスチェックのエンドポイントを定義する
@blue_print.route(route="health", methods=["GET"])
def health(req: func.HttpRequest) -> func.HttpResponse:
    return func.HttpResponse(
        body='{"status": "ok", "CI/CD": "OK"}',
        mimetype="application/json",
        status_code=200
    )