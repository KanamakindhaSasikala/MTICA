##coord=(3,5)
##abc=(2,9)
##type(coord)
##<class 'tuple'>
##type(abc)
##<class 'tuple'>
##abc[0]
##2
##print('x: {0[0]}; y: {0[1]};abc : {1[0]},{1[1]}'.format(coord,abc))
##x: 3; y: 5;abc : 2,9
##================================
##print('{:#<30}'.format('apple'))
##apple#########################
##print('{:*>30}'.format('apple'))
##*************************apple
##print('{:^30}'.format('apple'))
##            apple             
##print('{:*^30}'.format('apple'))
##************apple*************
##print('{:&^20}'.format('apple'))
##&&&&&&&apple&&&&&&&&
##&&&&&&&apple&&&&&&&&p
##SyntaxError: invalid syntax
##print('{:$^10}'.format('good'))
##$$$good$$$
##print('{:@^10}'.format('sasikala'))
##@sasikala@
##
##==========================================
##print("int: {0:d};  hex: {0:x}; oct:  {0:o};bin: {0:b}".format(42,55))
##int: 42;  hex: 2a; oct:  52;bin: 101010
##print("int: {1:d};  hex: {1:x}; oct:  {1:o};bin: {1:b}".format(42,55))
##int: 55;  hex: 37; oct:  67;bin: 110111
##print('{0:,}'.format(1234567890))
##1,234,567,890
##points=19.0; total=22
##print('correct answers:{:.2%},.format(points/total))
##      
##SyntaxError: unterminated string literal (detected at line 1)
##print('correct answers:{:.2%}'.format(points/total))
##      
##correct answers:86.36%
##print('correct answers:{:.2}'.format(points/total))
##      
##correct answers:0.86
##import time
##n=int(input("enter a no: "))
##start=time.time()
##for i in range(n):
##    print("i=",i,"i^2=",i*i)
##print("time taken by Loop:",(time.time()-strat)*100000)
##
##n=int(input())
##lst=[]
##for i in range(1,1001):
##     if i%8==0:
##         lst.append(i)
##print("lst,end=")
##print(len(lst))
##print(lst)
##
##ans=[]
##for i in range(1,1001):
##    if i%8==0:
##        ans.append(i)
##print(ans)
ans=[]
for i in range(900,1001):
     if '6' in str(i):
          ans.append(i)
print(ans)

                                                                                                    
