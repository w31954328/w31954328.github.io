from flask import Flask,request
from flask import render_template
from flask import jsonify
import utils


app = Flask(__name__)


@app.route('/',methods=["get","post"])
def my_tem():
    #在浏览器上渲染my_templaces.html模板
    # return render_template('text.html')
    return render_template('text_1.html')

@app.route("/page3_l1",methods=["get","post"])
def get_page3_l1_data():
    location=[]
    total_vaccinations=[]
    for tup in utils.get_page3_l1_data():
            location.append(tup[0])
            total_vaccinations.append(tup[1])
    print({"location":location,"total_vaccinations":total_vaccinations})
    return jsonify({"location":location,"total_vaccinations":total_vaccinations})



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run()
    # print(get_data())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/