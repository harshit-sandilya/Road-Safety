from core.Handler import Handler

obj = Handler("en")

print(obj.process_question("Which side of the road should I walk on?"))
print(obj.process_question("What is the speed limit in a residential area?"))
print(obj.process_question("What is the speed limit in a school zone?"))

obj = Handler("hi")

print(obj.process_question("सड़क के किस ओर चलना चाहिए?"))
print(obj.process_question("निवासी क्षेत्र में गति सीमा क्या है?"))
print(obj.process_question("स्कूल क्षेत्र में गति सीमा क्या है?"))

# 1-en model
# 2-hi model
