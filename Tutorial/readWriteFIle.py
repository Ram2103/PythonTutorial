with open('/Users/ramanathan/Documents/Automation/Selenium_PythonTutorial/sample', 'r') as read:
    line = read.readlines()
    for i in line:
        print(i)

    print("---------------------")
    with open('/Users/ramanathan/Documents/Automation/Selenium_PythonTutorial/sample', 'w') as writer:
        for j in reversed(line):
            writer.write(j)
            print(j)

file = open('/Users/ramanathan/Documents/Automation/Selenium_PythonTutorial/sample')
print(file.readlines())

assert ("abc" in "abc"), "incorrect"
