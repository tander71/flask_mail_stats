from flask import Flask, render_template
app = Flask(__name__)

with open("/home/tanderegg/Documents/list.txt") as f:
  content = f.readlines()
  content = [x.strip() for x in content]
  content = [x.split(";") for x in content]

@app.route('/')
def index():
    return render_template('index.html',
    mbox0=content[0][0],
    user0=content[0][1],
    free0=content[0][4],
    percent0=content[0][5],
    mbox1=content[1][0],
    user1=content[1][1],
    free1=content[1][4],
    percent1=content[1][5],
    mbox2=content[2][0],
    user2=content[2][1],
    free2=content[2][4],
    percent2=content[2][5],
    mbox3=content[3][0],
    user3=content[3][1],
    free3=content[3][4],
    percent3=content[3][5],
    mbox4=content[4][0],
    user4=content[4][1],
    free4=content[4][4],
    percent4=content[4][5],
    mbox5=content[5][0],
    user5=content[5][1],
    free5=content[5][4],
    percent5=content[5][5],
    mbox6=content[6][0],
    user6=content[6][1],
    free6=content[6][4],
    percent6=content[6][5],
    mbox7=content[7][0],
    user7=content[7][1],
    free7=content[7][4],
    percent7=content[7][5],
    mbox8=content[8][0],
    user8=content[8][1],
    free8=content[8][4],
    percent8=content[8][5],
    mbox9=content[9][0],
    user9=content[9][1],
    free9=content[9][4],
    percent9=content[9][5],
    mbox10=content[10][0],
    user10=content[10][1],
    free10=content[10][4],
    percent10=content[10][5],
    mbox11=content[11][0],
    user11=content[11][1],
    free11=content[11][4],
    percent11=content[11][5],
    mbox12=content[12][0],
    user12=content[12][1],
    free12=content[12][4],
    percent12=content[12][5],
    mbox13=content[13][0],
    user13=content[13][1],
    free13=content[13][4],
    percent13=content[13][5],
    mbox14=content[14][0],
    user14=content[14][1],
    free14=content[14][4],
    percent14=content[14][5],
    mbox15=content[15][0],
    user15=content[15][1],
    free15=content[15][4],
    percent15=content[15][5],
    mbox16=content[16][0],
    user16=content[16][1],
    free16=content[16][4],
    percent16=content[16][5],
    mbox17=content[17][0],
    user17=content[17][1],
    free17=content[17][4],
    percent17=content[17][5],
    mbox18=content[18][0],
    user18=content[18][1],
    free18=content[18][4],
    percent18=content[18][5],
    mbox19=content[19][0],
    user19=content[19][1],
    free19=content[19][4],
    percent19=content[19][5],
    mbox20=content[20][0],
    user20=content[20][1],
    free20=content[20][4],
    percent20=content[20][5],
    mbox21=content[21][0],
    user21=content[21][1],
    free21=content[21][4],
    percent21=content[21][5]
    )

if __name__ == '__main__':
    app.run()
