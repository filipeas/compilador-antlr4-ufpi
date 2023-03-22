.class public programa_final
.super java/lang/Object
.field public static numero I
.field public static n1 I
.field public static n2 I
.field public static m F
.method public static fatorial(I)I
.limit stack 5
.limit locals 300
iload 0
istore 6
ldc 1
istore 7
iload 6
iload 7
if_icmpgt true8
ldc 0
goto cmp_end8
true8:
ldc 1
cmp_end8:
istore 8
iload 8
ldc 0
if_icmpeq if_0
iload 0
istore 9
iload 0
istore 10
ldc 1
istore 11
iload 10
iload 11
isub
istore 12
iload 12
invokestatic programa_final.fatorial(I)I
istore 4
iload 9
iload 4
imul
istore 13
iload 13
ireturn
goto end_else_0
if_0:
ldc 1
istore 14
iload 14
ireturn
end_else_0:
return
.end method
.method public static mostrarMedia(IIF)V
.limit stack 5
.limit locals 300
iload 0
istore 19
iload 1
istore 20
iload 19
iload 20
iadd
istore 21
ldc 2
istore 22
iload 21
iload 22
idiv
istore 23
iload 23
istore 2
ldc "Resultado: "
astore 24
iload 2
istore 25
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 24
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 25
invokevirtual java/io/PrintStream/print(I)V
return
.end method
.method public static media(FF)F
.limit stack 5
.limit locals 300
ldc 0.0
fstore 29
fload 0
fstore 30
fload 1
fstore 31
fload 30
fload 31
fadd
fstore 32
ldc 2
istore 33
iload 33
i2f
fstore 33
fload 32
fload 33
fdiv
fstore 34
fload 34
fstore 29
fload 29
fstore 35
fload 35
freturn
return
.end method
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 0.0
fstore 36
ldc 0.0
fstore 37
bipush 0
istore 38
bipush 0
istore 39
ldc "Programa Fatorial. Digite o numero?"
astore 40
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 40
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextInt()I
istore 0
iload 0
putstatic programa_final/numero I
getstatic programa_final/numero I
istore 41
iload 41
invokestatic programa_final.fatorial(I)I
istore 4
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 4
invokevirtual java/io/PrintStream/print(I)V
ldc "Programa media. Digite os valores?"
astore 42
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 42
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextInt()I
istore 1
iload 1
putstatic programa_final/n1 I
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextInt()I
istore 2
iload 2
putstatic programa_final/n2 I
getstatic programa_final/n1 I
istore 43
getstatic programa_final/n2 I
istore 44
getstatic programa_final/m F
fstore 45
iload 43
iload 44
fload 45
invokestatic programa_final.mostrarMedia(IIF)V
ldc "Programa media v2. Digite os valores?"
astore 46
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 46
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 36
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 37
ldc "media calculada"
astore 47
fload 36
fstore 48
fload 37
fstore 49
fload 48
fload 49
invokestatic programa_final.media(FF)F
fstore 26
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 47
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 26
invokevirtual java/io/PrintStream/print(F)V
ldc 1
istore 50
ldc 0
istore 51
iload 50
iload 51
ior
istore 52
iload 52
ldc 0
if_icmpeq if_2
ldc "entrou no ||\n"
astore 53
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 53
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
goto end_else_2
if_2:
ldc "oloco"
astore 54
getstatic programa_final/n1 I
istore 55
ldc " "
astore 56
getstatic programa_final/n2 I
istore 57
ldc " "
astore 58
getstatic programa_final/m F
fstore 59
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 54
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 55
invokevirtual java/io/PrintStream/print(I)V
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 56
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 57
invokevirtual java/io/PrintStream/print(I)V
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 58
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 59
invokevirtual java/io/PrintStream/print(F)V
end_else_2:
iload 39
istore 60
ldc 10
istore 61
iload 60
iload 61
if_icmplt true62
ldc 0
goto cmp_end62
true62:
ldc 1
cmp_end62:
istore 62
ldc 1
istore 63
iload 63
ldc 1
ixor
istore 64
iload 62
iload 64
iand
istore 65
iload 65
ldc 0
if_icmpeq if_4
ldc "oloco\n"
astore 66
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 66
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
goto end_else_4
if_4:
ldc "oioioi\n\n"
astore 67
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 67
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
end_else_4:
iload 39
istore 38
test_for38:
iload 38
istore 68
ldc 10
istore 69
iload 68
iload 69
if_icmplt true70
ldc 0
goto cmp_end70
true70:
ldc 1
cmp_end70:
istore 70
ldc "entrou no for\n"
astore 71
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 71
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
iload 70
ldc 1
if_icmpeq check_incremento_38
goto exit_for_38
check_incremento_38:
iinc 38 +1
goto test_for38
exit_for_38:
ldc 0
istore 72
iload 72
istore 38
enter_while1:
iload 38
istore 74
ldc 10
istore 75
iload 74
iload 75
if_icmplt true76
ldc 0
goto cmp_end76
true76:
ldc 1
cmp_end76:
istore 76
iload 76
ldc 1
if_icmpne break1
ldc "entrou no while\n"
astore 77
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 77
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
iload 38
istore 78
ldc 1
istore 79
iload 78
iload 79
iadd
istore 80
iload 80
istore 38
goto enter_while1
break1:
return
.end method
