# кредит
s = int(input())
n = int(input())
k = int(input())
lst = []
for t in range(1,n+1):
    def compute_payment(t, s, n, k):
        plotech = round(s/n + (s - (t-1) * (s/n))*(k/(12*100)),2)
        lst.append(plotech)
        return plotech

for t in range(1,n+1):
    print("%2d месяц - %8.2f руб" % (t,compute_payment(t, s, n, k)))
doh_banka = sum(lst)-s
print("Доход банка - %6.2f руб" % doh_banka)


        