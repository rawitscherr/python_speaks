def define_function_with_params(stringer):
    stringArr = stringer.split(" ")
    index = 0
    functionNameArr = []
    varNameArr = []

    for i in range(0, len(stringArr)):
        if stringArr[i] == "function":
            for j in range (i + 1, len(stringArr)):
                if stringArr[j] == "of":
                    index = j
                    break
                functionNameArr.append(stringArr[j])
            for k in range (index + 1, len(stringArr)):
                if stringArr[k] == "and":
                    continue
                varNameArr.append(stringArr[k])
            break

    functionName = "_".join(functionNameArr)
    varName = ",".join(varNameArr)

    statement = "def " + functionName + "(" + varName + "):"

    print statement
    return statement

define_function_with_params("define function foo of x") #-> def foo(x)
define_function_with_params("define function this function of x and y") #-> def this_function(x,y)
define_function_with_params("define function foo of x y and z") #-> def foo(x,y,z)
