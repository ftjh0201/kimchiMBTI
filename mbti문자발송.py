import tkinter as tk
import tkinter.font
from tkinter import messagebox
from tkinter import simpledialog



mbti_type = {"INTJ": "용의주도한 전략가형", 
"INTP": "논리적인 사색가형",
"ENTJ": "대담한 통솔자형",
"ENTP": "뜨거운 논쟁을 즐기는 변론가형",
"ENFP": "재기발랄한 활동가형",
"ENFJ": "정의로운 사회 운동가형",
"INFP": "열정적인 중재자형",
"INFJ": "선의의 옹호자형",
"ESFJ": "사교적인 외교관형",
"ESTJ": "엄격한 관리자형",
"ISFJ": "용감한 수호자형",
"ISTJ": "청렴결백한 논리주의자형",
"ESFP": "자유로운 영혼의 연예인형",
"ESTP": "모험을 즐기는 사업가형",
"ISFP": "호기심 많은 예술가형",
"ISTP": "만능 재주꾼형"
}

mbti_job = {
"INTJ": "투자 은행원, 재무상담가, SW개발자",
"INTP": "프로그래머, 재무 분석가, 교수",
"ENTJ": "변호사, 경영 컨설턴트, 분석 전문가",
"ENTP": "기업가, 정치가, 마케팅 디렉터",
"ENFP": "저널리스트, 요식업 경영자, 파티플래너",
"ENFJ": "세일즈 매니저, 고용 전문가, PR 전문가",
"INFP": "그래픽 디자이너, 심리학자, 작가",
"INFJ": "치료사, 사회복지사, 고객 관계 매니저",
"ESFJ": "판매 대표자, 간호사, 헬스케어 종사자",
"ESTJ": "보험 세일즈맨, 약사, 프로젝츠 매니저",
"ISFJ": "치과의사, 사서, 초등학교 교사",
"ISTJ": "감리사, 회계사, 웹 개발자",
"ESFP": "아동 복지 상담가, 배우 , 디자이너",
"ESTP": "탐정, 은행원, 투자가",
"ISFP": "패션 디자이너, 물리치료사, 조경설계사",
"ISTP": "토목기사, 파일럿, 경제학자"}

mbti_good = {
"INTJ": "ESFP", 
"INTP": "ESFJ", 
"ENTJ": "ISFP", 
"ENTP": "ISFJ", 
"ENFP": "ISTJ", 
"ENFJ": "ISTP", 
"INFP": "ESTJ", 
"INFJ": "ESTP", 
"ESFJ": "INTP", 
"ESTJ": "INFP",  
"ISFJ": "ENTP", 
"ISTJ": "ENFP", 
"ESFP": "INTJ", 
"ESTP": "INFJ",  
"ISFP": "ENTJ", 
"ISTP": "ENFJ"    
}

mbti_bad = {
"INTJ": "ESFJ",
"INTP": "ESFP",
"ENTJ": "ISFJ",
"ENTP": "ISFP",
"ENFP": "ISTP",
"ENFJ": "ISTJ",
"INFP": "ESTP",
"INFJ": "ESTJ",
"ESFJ": "INTJ",
"ESTJ": "INFJ",
"ISFJ": "ENTJ",
"ISTJ": "ENFJ",
"ESFP": "INTP",
"ESTP": "INFP",
"ISFP": "ENTP",
"ISTP": "ENFP"    
}

def sms_send():
    global sms_result, hp
    print(sms_result)

    uid = "pythonapi" 
    upw = "1234"
    subject = "MBTI 검사결과"
    content = sms_result
    hpno = hp
    callback = "01012345678"

    jweb = smssend.JmunjaWeb(uid, upw)
    wresult = jweb.send(subject, content, hpno, callback)

    if wresult:
        label_smsresult['text'] = "발송 성공!"

def check():
    global sms_result
    # print("no1 : {} {} {} {}".format(radio_var1.get(), radio_var2.get(), radio_var3.get(), radio_var4.get()))

    ans1 = ""
    ans2 = ""
    ans3 = ""
    ans4 = ""

    if radio_var1.get() == 1: ans1 = "I"
    elif radio_var1.get() == 2: ans1 = "E"
    if radio_var2.get() == 1: ans2 = "T"
    elif radio_var2.get() == 2: ans2 = "F"
    if radio_var3.get() == 1: ans3 = "J"
    elif radio_var3.get() == 2: ans3 = "P"
    if radio_var4.get() == 1: ans4 = "S"
    elif radio_var4.get() == 2: ans4 = "N"

    if radio_var1.get() and radio_var2.get() and radio_var3.get() and radio_var4.get():
        result = ans1+ans4+ans2+ans3
        
        my_type = "["+result + "] " + mbti_type[result]
        my_job = mbti_job[result]
        my_good = mbti_good[result]
        my_bad = mbti_bad[result]

        label_9['text'] = my_type
        label_10['text'] = my_job
        label_11['text'] = my_good
        label_12['text'] = my_bad

        sms_result = name+"님의 MBTI 심리검사 결과입니다.\n\n" \
            "* 타입: "+my_type+"\n" \
            "* 직업: "+my_job+"\n" \
            "* 환상의궁합: "+my_good+"\n" \
            "* 최악의궁합: "+my_bad


window = tk.Tk()
window.title("MBTI 심리검사")
window.geometry("750x550")

answer = messagebox.askyesno("질문","신상정보를 입력하시겠습니까? 입력할 경우 검사결과를 문자로 받아보실 수 있습니다.")

if answer == True:
    name = simpledialog.askstring("입력", "이름을 입력해주세요.", parent=window)
    age = simpledialog.askstring("입력", "나이를 입력해주세요.", parent=window)
    sex = simpledialog.askstring("입력", "성별을 입력해주세요.(남성or여성)", parent=window)
    hp = simpledialog.askstring("입력", "휴대폰번호를 입력해주세요.(현재 사용 불가)", parent=window)
else:
    name = "익명"
    age = ""
    sex = ""
    hp = ""

sms_result = ""

font=tkinter.font.Font(family="맑은 고딕", size=18)
font2=tkinter.font.Font(family="맑은 고딕", size=11)

tk.Label(window, text="MBTI 심리검사 프로그램 Ver.SIMPLE", fg="blue", font=font).pack()

frame1 = tk.Frame(window)
frame1.pack()

label_sinsang = tk.Label(frame1, text=name+"("+age+", "+sex+", "+hp+")", anchor="w", width="60", font=font2, fg="green")
label_0 = tk.Label(frame1, text="※ 각 문항에 대해 예, 아니오로 답해주세요", anchor="w", width="60", font=font2)
label_1 = tk.Label(frame1, text="1. 다른 사람들에게 자신을 소개하는 것을 어려워 합니다.", anchor="w", width="60", font=font2)
label_2 = tk.Label(frame1, text="2. 논쟁에서 이기는 것이 상대방을 불쾌하지 않도록 하는 것보다 더 중요합니다.", anchor="w", width="60", font=font2)
label_3 = tk.Label(frame1, text="3. 적응을 잘 하는 것 보다 체계적인 것이 더 중요합니다.", anchor="w", width="60", font=font2)
label_4 = tk.Label(frame1, text="4. 본인이 창의적이기보다 현실적인 사람이라고 생각합니다.", anchor="w", width="60", font=font2)



label_sinsang.grid(row=0, column=0, padx=10, pady=5)
label_0.grid(row=1, column=0, padx=10, pady=5)
label_1.grid(row=2, column=0, padx=10, pady=5)
label_2.grid(row=3, column=0, padx=10, pady=5)
label_3.grid(row=4, column=0, padx=10, pady=5)
label_4.grid(row=5, column=0, padx=10, pady=5)

radio_var1 = tk.IntVar()
radio_var2 = tk.IntVar()
radio_var3 = tk.IntVar()
radio_var4 = tk.IntVar()

radio_1 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var1, command=check, font=font2)
radio_2 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var1, command=check, font=font2)
radio_3 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var2, command=check, font=font2)
radio_4 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var2, command=check, font=font2)
radio_5 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var3, command=check, font=font2)
radio_6 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var3, command=check, font=font2)
radio_7 = tk.Radiobutton(frame1, text="예", value="1", variable=radio_var4, command=check, font=font2)
radio_8 = tk.Radiobutton(frame1, text="아니오", value="2", variable=radio_var4, command=check, font=font2)

radio_1.grid(row=2, column=1, padx=10, pady=5)
radio_2.grid(row=2, column=2, padx=10, pady=5)
radio_3.grid(row=3, column=1, padx=10, pady=5)
radio_4.grid(row=3, column=2, padx=10, pady=5)
radio_5.grid(row=4, column=1, padx=10, pady=5)
radio_6.grid(row=4, column=2, padx=10, pady=5)
radio_7.grid(row=5, column=1, padx=10, pady=5)
radio_8.grid(row=5, column=2, padx=10, pady=5)

tk.Label(window, text="").pack()

frame2 = tk.Frame(window)
frame2.pack()

label_blank = tk.Label(frame2, text="")
label_5 = tk.Label(frame2, text="타입", width=10, height=1, anchor="w", font=font2, fg="red")
label_6 = tk.Label(frame2, text="직업", width=10, height=1, anchor="w", font=font2, fg="red")
label_7 = tk.Label(frame2, text="환상의궁합", width=10, height=1, anchor="w", font=font2, fg="red")
label_8 = tk.Label(frame2, text="최악의궁합", width=10, height=1, anchor="w", font=font2, fg="red")
label_9 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)
label_10 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)
label_11 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)
label_12 = tk.Label(frame2, text="", width=65, height=1, anchor="w", fg="blue", font=font2)

label_5.grid(row=0, column=0, padx=10, pady=1)
label_6.grid(row=1, column=0, padx=10, pady=1)
label_7.grid(row=2, column=0, padx=10, pady=1)
label_8.grid(row=3, column=0, padx=10, pady=1)
label_9.grid(row=0, column=1, padx=10, pady=1)
label_10.grid(row=1, column=1, padx=10, pady=1)
label_11.grid(row=2, column=1, padx=10, pady=1)
label_12.grid(row=3, column=1, padx=10, pady=1)
label_blank.grid(row=4, column=0, padx=10, pady=1)

# 문자발송
label_sms = tk.Label(window, text="검사결과를 문자로 받고 싶으시면 눌러주세요.", width=50, height=1, anchor="w", font=font2)
btn_sms = tk.Button(window, text="결과 문자받기(서버장애)", command=sms_send, width=20, height=1, fg="red", font=font2)
label_smsresult = tk.Label(window, text="", width=50, height=1, font=font2, fg="red")

if hp != "" and hp.startswith("010"):
    label_sms.pack()
    btn_sms.pack()
    label_smsresult.pack()

window.mainloop()
