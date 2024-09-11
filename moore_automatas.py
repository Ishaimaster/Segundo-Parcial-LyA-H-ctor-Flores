

class Moore:

    def State00 (token):

        if token == "variable":

            return 1

        else:
            print("Token no valido, se esperaba 'variable' no " + token)
            return -1

    def State01(token):
        if token == "=":
            return 2
        else:
            print("Token no valido, se esperaba '=' no " + token)
            return -1

    def State02(tokens,index):

        if index >= len(tokens):
            raise Exception("Cadena incompleta, se esperaba un numero")

        token = tokens[index]

        index_future = index

        t = " "

        if token in "01":

            while(index_future < len(tokens) - 1):

                next_token = tokens[index_future + 1]

                temp = ""

                if next_token in "01234567":

                    temp = next_token
                else:
                    print("Token invalido, no se esperaba " + next_token)
                    return -1, 0

                if temp > t:

                    t = temp

                index_future += 1

            if t in "23":

                return 5, index + 1

            elif t in "4567":

                return 4, index + 1


            return 3, index + 1

        elif token in "23":

            while(index_future < len(tokens) - 1):

                next_token = tokens[index_future + 1]

                if next_token in "4567":

                    return 4, index + 1

                elif next_token in "0123":

                    index_future += 1

                else:
                    print("Token invalido, no se esperaba " + next_token)
                    return -1, 0

            return 5, index + 1

        elif token in "4567":

            return 4, index + 1

        else:
            print("Token invalido, no se esperaba " + token)
            return -1, 0

    def State03(tokens, index):

        token = tokens[index]

        if token in "01":

            return 3, index + 1

        else:
            print("Token invalido, no se esperaba " + token)
            return -1, 0


    def State04(tokens, index):

        token = tokens[index]

        if token in "01234567":

            return 4, index + 1

        else:
            print("Token invalido, no se esperaba " + token)
            return -1, 0



    def State05(tokens, index):

     token = tokens[index]

     if token in "0123":

        return 5, index + 1

     else:
        print("Token invalido, no se esperaba " + token)
        return -1, 0



    def Moore_Machine (tokens):

        state_functions = {

            0: Moore.State00,
            1: Moore.State01,
            2: Moore.State02,
            3: Moore.State03,
            4: Moore.State04,
            5: Moore.State05

        }

        actual_state = 0

        index = 0

        var = " "

        while index < len(tokens):

            if actual_state in [0,1]:
                actual_state = state_functions[actual_state](tokens[index])
                index += 1

            elif actual_state == -1:
                break;

            else:
                actual_state, index = state_functions[actual_state](tokens, index)


        if actual_state in [3,4,5]:

            if actual_state == 3:
                var = "Binario"

            elif actual_state == 4:
                var = "Octal"

            else:
                var = "Base Cuatro"

            print("Expresion aceptada: el numero ingresado es " + var)

        else:

            print("Expresion no aceptada")










