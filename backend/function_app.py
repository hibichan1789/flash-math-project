import azure.functions as func
from api.health import blue_print as health_blue_print
from api.answers import answer_blueprint
from api.questions import questions_blueprint

# ルーティングを書く
app = func.FunctionApp()

# apiフォルダ以下のルーティングをどんどん登録していく
app.register_blueprint(health_blue_print)
app.register_blueprint(answer_blueprint)
app.register_blueprint(questions_blueprint)