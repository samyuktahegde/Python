def calculate_span(price, S):
    n = len(price)
    st = []
    st.append(0)
    S[0] = 1
    for i in range(1, n):
        while (len(st)>0 and price[st[0]]<=price[i]):
            st.pop()
        S[i] = i+1 if len(st)<=0 else (i-st[0])
        st.append(i)

price = [10, 4, 5, 90, 120, 80]
S = [0 for i in range(len(price)+1)]
 
# Fill the span values in array S[]
calculate_span(price, S)
print(S)