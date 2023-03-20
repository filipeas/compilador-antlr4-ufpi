from Erros import ErroVariavelNaoEncontradaNaTabelaDeSimbolo

class Generator:
    MAX_LOCALS = 300

    def __init__(self, nome_arquivo, tabela_simbolo):
        self.nome_arquivo = nome_arquivo
        self.file = open(nome_arquivo + '.j', 'w+')
        self.start_file()
        self.tabela_simbolo = tabela_simbolo
        self.top_index = 0
        self.label_count = 0

    def close_file(self):
        self.file.close()

    # remove tabs de strings antes de escrever a linha
    def __write(self, string):
        for s in string.split('\n'):
            if s.strip():
                self.file.write(s.strip() + "\n")

    def getVar(self, var_name, controle_escopo):
        if self.tabela_simbolo[var_name]:
            variable = self.tabela_simbolo[var_name]
        else:
            raise ErroVariavelNaoEncontradaNaTabelaDeSimbolo(var_name, controle_escopo)

        return variable

    def create(self, var_name, var_type, controle_escopo, const: False, val: 0):
        variable = self.getVar(var_name, controle_escopo)
        if controle_escopo:
            if var_type == 'bool' and val == 'true':
                val = 1
            elif var_type == 'bool' and val == 'false':
                val = 0
            elif var_type == 'real' and val == 0:
                val = 0.0
            elif var_type == 'String' and val == 0:
                val = "\"\""
            # fazer instancia de variavel local
            if variable.type == 'int' or variable.type == 'bool':
                self.__write(
                    """
                    bipush {}
                    istore {}
                    """.format(val, variable.address)
                )
            elif variable.type == 'real':
                self.__write(
                    """
                    ldc {}
                    fstore {}
                    """.format(val, variable.address)
                )
            elif variable.type == 'String':
                self.__write(
                    """
                    ldc {}
                    astore {}
                    """.format(val, variable.address)
                )
        else:
            # fazer instancia de variavel global
            if const:
                if var_type == 'bool' and val == 'true':
                    val = 1
                elif var_type == 'bool' and val == 'false':
                    val = 0
                self.__write(
                    """
                    .field public static final {} {} = {}
                    """.format(var_name, type_convert(var_type), val)
                )
            else:
                self.__write(
                    """
                    .field public static {} {}
                    """.format(var_name, type_convert(var_type))
                )

    def start_file(self):
        self.__write(
            """
            .class public {}
            .super java/lang/Object
            """.format(self.nome_arquivo)
        )

    def enter_main(self):
        self.__write(
            """
            .method public static main([Ljava/lang/String;)V
            .limit stack 10
            .limit locals {}
            """.format(self.MAX_LOCALS)
        )

    def exit_main(self):
        self.__write(
            """
            return
            .end method
            """
        )

    def enter_function(self, name, parameters):  # TODO: receive parameters
        param = ''
        for p in parameters:
            param += type_convert(self.tabela_simbolo[p].type)

        self.__write(
            """
            .method public static {}({}){}
            .limit stack 5
            .limit locals {}
            """.format(name, param, type_convert(self.tabela_simbolo[name].type), self.MAX_LOCALS)
        )
        for idx, p in enumerate(parameters):
            self.tabela_simbolo[p].address = idx
            self.tabela_simbolo[p].local = True

    def exit_function(self):
        self.__write(
            """
            return
            .end method
            """
        )

    def function_call(self, func_name, params, types):
        variable = self.tabela_simbolo[func_name]
        args = ''
        for p, t in zip(params, types):
            self.load_temp(p, t)
            args += type_convert(t)
        self.__write(
            """
            invokestatic {}.{}({}){}
            """.format(self.nome_arquivo, func_name, args, type_convert(variable.type))
        )
        return self.store_val(variable.type, variable.address)

    def do_return(self, val, type):
        return_type = type_convert(type)
        if (return_type == 'V'):
            self.__write(
                """
                return
                """
            )
            return

        self.load_temp(val, type)
        if return_type == 'I' or return_type == 'Z':
            self.__write(
                """
                ireturn
                """
            )
        elif return_type == 'F':
            self.__write(
                """
                freturn
                """
            )
        elif return_type == 'V':
            self.__write(
                """
                return
                """
            )
        elif return_type == 'Ljava/lang/String;':
            self.__write(
                """
                areturn
                """
            )

    def print(self, type_val):
        for type, val in type_val:
            self.__write(
                """
                getstatic java/lang/System/out Ljava/io/PrintStream;
                """
            )
            self.load_temp(val, type)
            self.__write(
                """
                invokevirtual java/io/PrintStream/print({})V
                """.format(type_convert(type))
            )

    def mul(self, type, addr1, addr2, addr3):
        self.load_temp(addr1, type)
        self.load_temp(addr2, type)
        if type == 'int':
            self.__write(
                """
                imul
                """
            )
        elif type == 'real':
            self.__write(
                """
                fmul
                """
            )
        return self.store_val(type, addr3)

    def div(self, type, addr1, addr2, addr3):
        self.load_temp(addr1, type)
        self.load_temp(addr2, type)
        if type == 'int':
            self.__write(
                """
                idiv
                """
            )
        elif type == 'real':
            self.__write(
                """
                fdiv
                """
            )
        return self.store_val(type, addr3)

    def calc_minus(self, type, addr1, addr3):
        self.load_temp(addr1, type)
        if type == 'int':
            self.__write(
                """
                bipush -1
                imul
                """
            )
        elif type == 'real':
            self.__write(
                """
                ldc -1
                fmul
                """
            )
        return self.store_val(type, addr3)

    def calc_not(self, val, addr):
        self.load_temp(val, 'bool')
        self.__write(
            """
            ldc 1
            ixor
            """
        )
        return self.store_val('bool', addr)

    def calc_and(self, val1, val2, addr):
        self.load_temp(val1, 'bool')
        self.load_temp(val2, 'bool')
        self.__write(
            """
            iand
            """
        )
        return self.store_val('bool', addr)

    def calc_or(self, val1, val2, addr):
        self.load_temp(val1, 'bool')
        self.load_temp(val2, 'bool')
        self.__write(
            """
            ior
            """
        )
        return self.store_val('bool', addr)

    def calc_eq(self, type, val1, val2, addr3, op):
        cmp = {'==': 'eq', '!=': 'ne', '>=': 'ge', '>': 'gt', '<=': 'le', '<': 'lt'}
        self.load_temp(val1, type)
        self.load_temp(val2, type)
        if type in ['int', 'bool']:
            self.__write(
                """
                if_icmp{} true{}
                """.format(cmp[op], addr3)
            )
        elif type == 'float':
            self.__write(
                """
                if{} true{}
                """.format(cmp[op], addr3)
            )
        else:
            self.__write(
                """
                if_acmp{} true{}
                """.format(cmp[op], addr3)
            )
        self.__write(
            """
            ldc 0
            goto cmp_end{}
            true{}:
            ldc 1
            cmp_end{}:
            """.format(addr3, addr3, addr3, addr3)
        )
        return self.store_val('bool', addr3)

    def store_val(self, type, addr):
        if type == 'String':
            self.__write(
                """
                astore {}
                """.format(addr)
            )
        elif type == 'int' or type == 'bool':
            self.__write(
                """
                istore {}
                """.format(addr)
            )
        elif type == 'real':
            self.__write(
                """
                fstore {}
                """.format(addr)
            )
        return addr

    def push_val(self, type, addr):
        # self.top_index -= 1
        if type == 'String':
            self.__write(
                """
                bapush {}
                """.format(addr)
            )
        elif type == 'int' or type == 'bool':
            self.__write(
                """
                bipush {}
                """.format(addr)
            )
        elif type == 'real':
            self.__write(
                """
                bfpush {}
                """.format(addr)
            )
        # self.top_index += 1
        return self.top_index # - 1

    def load_var(self, var, controle_escopo, addr):
        var_data = self.tabela_simbolo[var]

        if controle_escopo:
            if var_data.type == 'int' or var_data.type == 'bool':
                self.__write(
                    """
                     iload {}
                     """.format(var_data.address)
                )
            elif var_data.type == 'real':
                self.__write(
                    """
                    fload {}
                    """.format(var_data.address)
                )
            elif var_data.type == 'String':
                self.__write(
                    """
                    aload {}
                    """.format(var_data.address)
                )
        else:
            self.__write(
                """
                getstatic {}/{} {}
                """.format(self.name, var, type_convert(var_data.type))
            )
        return self.store_val(var_data.type, addr)

    def store_var(self, var, val, address, controle_escopo):
        var_data = self.getVar(var, controle_escopo)

        if controle_escopo:
            if var_data.type == 'int' or var_data.type == 'bool':
                self.__write(
                    """
                    iload {}
                    istore {}
                    """.format(val, address)
                )
            elif var_data.type == 'real':
                self.__write(
                    """
                    fload {}
                    fstore {}
                    """.format(val, address)
                )
            elif var_data.type == 'String':
                self.__write(
                    """
                    aload {}
                    astore {}
                    """.format(val, address)
                )
        else:
            self.load_temp(address, var_data.type)
            self.__write(
                """
                putstatic {}/{} {}
                """.format(self.nome_arquivo, var, type_convert(var_data.type))
            )

    def input(self, name, controle_escopo):
        table = self.tabela_simbolo[name]
        t = table.type

        self.__write(
            """
            new java/util/Scanner
            dup
            getstatic java/lang/System/in Ljava/io/InputStream;
            invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
            """
        )
        if t == 'String':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextLine()Ljava/lang/String;
                """
            )
        elif t == 'int':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextInt()I
                """.format(type_convert(table.type))
            )
        elif t == 'real':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextFloat()F
                """.format(type_convert(table.type))
            )
        elif t == 'bool':
            self.__write(
                """
                invokevirtual java/util/Scanner/nextBoolean()Z
                """.format(type_convert(table.type))
            )
        addr = self.store_val(table.type, table.address)
        # table.address = addr
        # self.store_var(name, table.address, controleTabelaFuncao)

    def add(self, type, addr1, addr2, addr3):
        self.load_temp(addr1, type)
        self.load_temp(addr2, type)
        if type == 'int':
            self.__write(
                """
                iadd
                """
            )
        elif type == 'real':
            self.__write(
                """
                fadd
                """
            )
        # concatenar string (descobrir como concatena string)
        return self.store_val(type, addr3)

    def sub(self, type, addr1, addr2, addr3):
        self.load_temp(addr1, type)
        self.load_temp(addr2, type)
        if type == 'int':
            self.__write(
                """
                isub
                """
            )
        elif type == 'real':
            self.__write(
                """
                fsub
                """
            )
        return self.store_val(type, addr3)

    def load_temp(self, val, type):
        if type == 'int' or type == 'bool':
            self.__write(
                """
                iload {}
                """.format(val)
            )
        elif type == 'real':
            self.__write(
                """
                fload {}
                """.format(val)
            )
        elif type == 'String':
            self.__write(
                """
                aload {}
                """.format(val)
            )

    def create_temp(self, val, type, addr):
        self.__write(
            """
            ldc {}
            """.format(val)
        )
        return self.store_val(type, addr)

    def int_to_float(self, addr):
        self.load_temp(addr, "int")
        self.__write(
            """
            i2f
            """
        )
        return self.store_val("real", addr)

    def getAddress(self, var, controleTabelaFuncao):
        var_data = self.symbol_table_local[var] if controleTabelaFuncao else self.symbol_table[var]
        return var_data.address

    def enter_while(self, loop_idx):
        self.__write(
            """
            enter_while{}:
            """.format(loop_idx)
        )
        return "iload {}\n" + "ldc 1\nif_icmpne break{}".format(loop_idx)

    def exit_while(self, loop_idx):
        self.__write(
            """
            goto enter_while{}
            break{}:
            """.format(loop_idx, loop_idx)
        )

    def enter_for(self, val, id, temBreak, controle_escopo):
        variable = self.tabela_simbolo[id]

        if controle_escopo:
            # local
            self.__write(
                """
                ldc {}
                istore {}
                test_for{}:
                {}
                """.format(val, variable.address, variable.address, "goto exit_for_{}".format(variable.address) if temBreak else '')
            )

        # return "for{}:\n goto test_for{}\n enter_for{}:\n".format(loop_idx, loop_idx, loop_idx)

    def exit_for(self, id, addr, op_incremento, incremento, controle_escopo):
        variable = self.getVar(id, controle_escopo)

        self.__write(
            """
            iload {}
            ldc 1
            if_icmpeq check_incremento_{}
            goto exit_for_{}
            check_incremento_{}:
            iinc {} {}{}
            goto test_for{}
            exit_for_{}:
            """.format(addr, variable.address, variable.address, variable.address, variable.address, op_incremento, incremento, variable.address, variable.address)
        )


        # val = self.load_var(id, controle_escopo, variable.address)
        # self.__write(
        #     """
        #     iinc {} +1
        #     """.format(val)
        # )
        # self.store_var(id, val, variable.address, controle_escopo)
        # self.__write(
        #     """
        #     goto for{}
        #     test_for{}:
        #     """.format(loop_idx, loop_idx)
        # )
        # val = self.load_var(id, controle_escopo, variable.address)
        # self.load_temp(val, 'int')
        # self.load_temp(end, 'int')
        # self.__write(
        #     """
        #     if_icmpge break{}
        #     goto enter_for{}
        #     break{}:
        #     """.format(loop_idx, loop_idx, loop_idx)
        # )

    def break_loop(self, break_point):
        self.__write(
            """
            goto exit_for_{}
            """.format(break_point)
        )

    def write_inh(self, line):
        self.__write(line)

    def enter_if(self, id):
        self.load_temp(id, 'int')
        self.__write(
            """
            ldc 0
            if_icmpeq if_{}
            """.format(self.label_count, self.label_count)
        )
        self.label_count += 1
        return self.label_count - 1

    def enter_else(self):
        self.__write(
            """
            goto end_else_{}
            if_{}:
            """.format(self.label_count - 1, self.label_count - 1)
        )
        self.label_count += 1
        return self.label_count - 1

    def make_label(self, label_name):
        self.__write(
            """
            {}:
            """.format(label_name)
        )

class Id:
    def __init__(self, address: int = None, type=None, scope=None, function: bool = False, local: bool = False):
        self.type = type
        self.scope = scope # False: global | True: local
        self.address = address
        self.function = function
        self.local = local

    def printId(self):
        print("tipo: ", self.type)
        print("escopo: ", self.scope)
        print("endereco: ", self.address)
        print("funcao: ", self.function)
        print("local: ", self.local)

def type_convert(type):
    descriptor = {'int': 'I', 'real': 'F', 'String': 'Ljava/lang/String;', 'bool': 'Z', None: 'V'}
    # print('type: ', type, descriptor[type])
    if type != 'int' and type != 'real' and type != 'String' and type != 'bool' and type != None:
        return descriptor[type.type]
    else:
        return descriptor[type]