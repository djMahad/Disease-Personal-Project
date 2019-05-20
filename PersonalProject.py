Arthritis = "\n\nYou most likely have Arthritis. This is a medical condition that damages the body's joints, causing discomfort and pain. It can range from mild to severe and can affect people of all ages. Arthritis most often develops in adults who are in their late 40’s or older and it is also more common in women and other people with a family history of the condition. It affects the joints of the body making movement more difficult thus causing pain and stiffness. It also causes swelling and the formation of bony spurs. Bones also start to rub with other bones altering the shape of the joint thus making it easier for the bone to pop out. The most commonly affected joints are hands, spine, knees and hips. Some symptoms of this disease include; join pain, tenderness, inflammation, restricted movement and weakness of bones. Although there is no cure for arthritis there are many treatment to slow it down. For mild to medium arthritis: Painkillers, physiotherapy and regular exercise can help reduce/slow down the effects, and for severe conditions, surgery such as: Arthroplasty, arthrodesis and osteotomy is recommended."
Asthma = "\n"
Commoncold = "\n"
Cough = "\n"
Diarrhoea = "\n"
FLu = "\n"
Foodpoisoning = "\n"
Hayfever = "\n"
Whoppingcough = "\n"
B12defficency = "\n"
Irondefficency = "\n"
Foodallergies = "\n"

print("\n                                                      WELCOME TO THE DISEASE DIAGNOSTICS PROGRAM")
begin = input("\n                                      Would you like to begin?: ")
if begin == "yes" or begin == "Yes" or begin == "YES":
    print("\n\n\n                                   Choose one of the options below for all the following question")
    print("\n\n                                       YES")
    print("\n                                       NO")
    Q1 = input("\n\n\n                              Do you feel pain in your joints/weakness in your bones?: ")
    if Q1 == "yes" or Q1 == "Yes" or Q1 == "YES":
        print(Arthritis)
    else:
        Q2 = input("\n\n\n                              Do you have headaches often")
        print(                             Q2)
else:
    print("\n                                         THANKS FOR TRYING OUT THE DISEASE DIAGNOSTIC PROGRAM!")
 
