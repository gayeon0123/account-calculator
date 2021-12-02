from tkinter import*
import tkinter.font

root = Tk()
# 윈도우창의 제목을 변경
root.title("예적금○△□을 시작합니다!")

#텍스트에 폰트와 padding을 지정할 수 있다.
titleFont=tkinter.font.Font(family="맑은 고딕", size=20, weight="bold", slant="italic")
titleLabel = Label(root, text="예적금○△□을 시작합니다!", font=titleFont, fg="#424242", pady="5").pack()

#시작화면 이미지
wall = PhotoImage(file = "ma.png")
wall_label = Label(image = wall)
wall_label.place(x = 0, y = 150)

# 버튼1 (상품 추천받기) 클릭 시
def recom():
    global recomm
    
    recomm=Toplevel() #새 창 띄우기
    recomm.title("상품 추천") #새 창 이름

    label0=Label(recomm, width=50, height=5) #Label을 통해 left 배치가 쉬워지도록 함
    label0.pack() 

    bank1=Button(label0, text = '하나은행', command = click_h1).pack(side=LEFT, padx=10) #은행 버튼생성
    bank2=Button(label0, text = '국민은행', command = click_g1).pack(side=LEFT, padx=10)
    bank3=Button(label0, text = '신한은행', command = click_s1).pack(side=LEFT, padx=10)
    
#하나은행 선택시
def click_h1(): #예금, 적금 버튼 생성
    label1=Label(recomm, width=50, height=5)
    label1.pack()
    Yh1=Button(label1, text = '예금', command=click_hy).pack(side=LEFT, padx=10)
    Jh1=Button(label1, text = '적금', command=click_hj).pack(side=LEFT, padx=10)

def click_hy(): #예금 버튼을 눌렀을 때 관련 정보 출력
    label_hy1=Label(recomm, text="<3.6.9 정기예금>\n3개월마다 높은 금리로 갈아탈 수 있는 옵션 보너스 제공\
    \n입출금과 거치식 예금의 장점만을 모은 편리하고 유용한 상품\
    \n내집마련, 결혼, 출산 등 기쁜 날 해지 시 해당 기간별 고시 이율 적용\n가입대상: 실명의 개인/개인사업자\
    \n예금종류: 정기예금\n가입기간: 1년제\n최저가입금액: 3백만원 이상\n최대금리: 연 0.95%")
    label_hy1.pack()
    label_hy2=Label(recomm, text="<행복 knowhow연금예금>\n매달 수령하는 원리금을 생활자금으로 이용\n만기수령금액은 언제든지 변경 가능\
    \n가입대상: 실명의 개인/개인사업자\n예금종류: 정기예금\n가입기간: 1년~31년\n최저가입금액:1백만원 이상\n최고금리: 연 1.10%")
    label_hy2.pack()

def click_hj(): #적금 버튼을 눌렀을 때 관련 정보 출력
    label_hy1=Label(recomm, text="<하나 타이밍 적금>\n게임하듯 재밌게 타이밍 버튼을 터치하여 저축시 우대금리가 제공됨\
    \n가입대상: 실명의 개인/개인사업자\n가입기간: 6개월\n가입금액:1천원 이상 20만원 이하\n금리: 최대 연 1.70%")
    label_hy1.pack()
    label_hj2=Label(recomm, text="<도전365적금>\n하나멤버스 연동 자신의 걸음수에 따라 우대금리 혜택을 받는 적금\
    \n[걸음수 특정]\n- 안드로이드: 삼성헬스 지원이 가능한 기기에서 사용가능\
    \n- 아이폰(iOS 8.0 이상의 기기에서 사용가능\n  (단, 아이폰 5C 이하 기기는 사용불가)\
    \n가입대상: 만 14세 이상 실명의 개인 및 개인사업자\n가입기간: 1년\n가입금액/적립한도: 1천원 이상 20만원 이하\n최대금리: 연 2.25%")
    label_hj2.pack()
    label_hj3=Label(recomm, text="<주거래하나 월복리 적금>\n공과금, 카드대금 이체 등 각종 주거래 건수에 따라 우대금리가 제공되는 월복리 적금\
    \n가입대상: 실명의 개인/개인사업자\n가입기간: 1/2/3년\n가입금액/적립한도: 1만원 이상 300만원 이하\n최대금리: 연 2.50%")
    label_hj3.pack()

   
#국민은행 선택시
def click_g1(): #예금, 적금 버튼 생성
    label1=Label(recomm, width=50, height=5)
    label1.pack()
    Yh1=Button(label1, text = '예금', command=click_gy).pack(side=LEFT, padx=10)
    Jh1=Button(label1, text = '적금', command=click_gj).pack(side=LEFT, padx=10)

def click_gy(): #예금 버튼을 눌렀을 때 관련 정보 출력
    label_gy1=Label(recomm, text="<KB Green Wave 1.5℃ 정기예금>\n가입대상: 개인 및 개인 사업자\
    \n계약기간: 1년제\n가입금액: 1백만원 이상 1천만원 이하\n이자지급: 만기일시지급식\n이자: 연 1.4%")
    label_gy1.pack()
    label_gy2=Label(recomm, text="<KB펀드와 만나는 예금>\n가입대상: 개인 및 개인사업자\n계약기간: 6개월 이상 36개월 이하\n가입금액: 3백만원 이상\
    \n이자지급: 만기일시지급+원리균등분할지급\n이자: 연 1.15%")
    label_gy2.pack()

def click_gj(): #적금 버튼을 눌렀을 때 관련 정보 출력
    label_gj1=Label(recomm, text="<KB 내 맘대로 적금>\n가입대상: 실명의 개인\n계약기간: 6개월 이상 36개월 이하\
    \n가입금액: 1만원 이상\n이자지급: 만기일시지급식\n이자: 연 2.25%")
    label_gj1.pack()
    label_gj2=Label(recomm, text="<KB 국민 프리미엄 적금(자유적립식)\n가입대상: 실명의 개인\n계약기간: 12개월~60개월\
    \n가입금액: 월 1만원 ~3백만원\n이자지급: 만기일시지급식\n이자: 연 2.95%")
    label_gj2.pack()
    label_gj3=Label(recomm, text="<KB 리브와 함께 매일매일 적금>\n가입대상: 리브(Liiv)를 가입한 만 17세 이상 실명의 개인\n계약기간: 6개월\
    \n가입금액: 1천원 이상 30만원\n이자지급: 만기일시지급식\n이자: 연 1.55%")
    label_gj3.pack()

                    
#신한은행 선택시
def click_s1(): #예금, 적금 버튼 생성
    label1=Label(recomm, width=50, height=5)
    label1.pack()
    Yh1=Button(label1, text = '예금', command=click_sy).pack(side=LEFT, padx=10)
    Jh1=Button(label1, text = '적금', command=click_sj).pack(side=LEFT, padx=10)

def click_sy(): #예금 버튼을 눌렀을 때 관련 정보 출력  
    label_sy1=Label(recomm, text="<쏠편한 정기예금>\n가입대상: 개인부분, 기타 임의 단체\
    \n가입기간: 1년\
    \n가입금액: 1만원부터 제한없음\n이자: 연 1.45%")
    label_sy1.pack()
    label_sy2=Label(recomm, text="<신한 S드림 정기예금>\n가입대상: 제한없음\
    \n가입기간: 1개월 이상 60개월 이하 1일 단위\
    \n가입금액: 300만원부터 제한없음\n이자: 연 0.85%")
    label_sy2.pack()

def click_sj(): #적금 버튼을 눌렀을 때 관련 정보 출력   
    label_sj1=Label(recomm, text="<신한 스마트 적금>\n가입대상: 개인부분\n가입기간: 12개월\
    \n가입금액: 1천원부터 100만원까지\n이자: 연 1.8%")
    label_sj1.pack()
    label_sj2=Label(recomm, text="<신한 S드림(Dream)적금>\n가입대상: 개인부분\n가입기간: 6개월 이상 60개월 이하 1개월 단위\
    \n가입금액: 1천원부터 제한없음\
    \n이자: 연 0.85%~연1.25%")
    label_sj2.pack()
    label_sj3=Label(recomm, text="<신한 새희망 적금>\n가입대상: 개인부분\n가입기간: 36개월\
    \n가입금액: 1천원부터 20만원까지\n이자: 연 1.8%")
    label_sj3.pack()
    label_sj4=Label(recomm, text="<마이홈플랜 주택청약종합저축>\n가입대상: 개인부분\
    \n가입기간: 840개월\n가입금액: 2만원부터 1,500만원까지(10원 단위)\n이자: 연 1.8%")
    label_sj4.pack()

    

# 버튼2 (금리 계산기) 클릭 
def calcul():
    Calc=Toplevel() #새 창 띄우기
    Calc.title("금리 계산기") #새 창 이름 
    Calc.geometry("570x400")

    global e1
    global e2
    global e3
    global e4
    global e5
    
    l1=Label(Calc, text="원금(원)")  #Label 위젯 1~5 생성   변수l = 항목 이름
    l2=Label(Calc, text="이자율")
    l3=Label(Calc, text="예치할 햇수(년)")
    l4=Label(Calc, text="단리 계산 원리금(원)")
    l5=Label(Calc, text="복리 계산 원리금(원)")
    l1.pack()
    l2.pack()
    l3.pack()
    l4.pack()
    l5.pack()
    l1.place(x=120,y=40)
    l2.place(x=120,y=80)
    l3.place(x=120,y=120)
    l4.place(x=120,y=270)
    l5.place(x=120,y=310)

    e1=Entry(Calc)
    e2=Entry(Calc)
    e3=Entry(Calc)
    e4=Entry(Calc)
    e5=Entry(Calc)
    e1.pack()
    e2.pack()
    e3.pack()
    e4.pack()
    e5.pack()
    e1.place(x=280,y=40)
    e2.place(x=280,y=80)
    e3.place(x=280,y=120)
    e4.place(x=280,y=270)
    e5.place(x=280,y=310)

    b1=Button(Calc, text="계산 결과 보기", command=cal)   #b = 변수
    b2=Button(Calc, text="다 지우기", command=delete)
    b1.pack()
    b2.pack()
    b1.place(x=135,y=200)
    b2.place(x=300,y=200)

def cal(): #계산식        #변수e = 입력받을 숫자 
    A=float(e1.get())
    r=float(e2.get())
    n=float(e3.get())
    s_total=float(A * (1 + r / 100 * n)) #단리 계산식
    c_total=float(A* (1 + r / 100)** n) #복리 계산식
    e4.insert(0,s_total) 
    e5.insert(0,c_total)

def delete():
    e1.delete(0,'end')  
    e2.delete(0,'end')
    e3.delete(0,'end')
    e4.delete(0,'end')
    e5.delete(0,'end')    

# 버튼
main_Font = tkinter.font.Font(size=10, weight="bold")
main_Label = Label(root, text="원하시는 서비스 버튼을 클릭해 주세요! ^^", pady="5", font=main_Font).pack()
Button1 = Button(root, text="금융 상품 추천받기", command=recom, width=20, pady="5").pack()
Button2 = Button(root, text="금리 계산하기", command=calcul,  width=20, pady="5").pack()

#result 
resultLabel = Label(root, text="")
resultLabel.pack(pady=10)

#윈도우 사이즈 설정
root.geometry("570x400")

#기본 루프
root.mainloop()
