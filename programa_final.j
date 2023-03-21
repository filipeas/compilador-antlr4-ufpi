.class public programa_final
.super java/lang/Object
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
bipush 0
istore 0
bipush 0
istore 1
bipush 0
istore 2
ldc "lanca 2 valor pra nois:"
astore 3
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 3
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextInt()I
istore 0
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextInt()I
istore 1
iload 0
istore 4
iload 1
istore 5
ldc 7
istore 6
iload 5
iload 6
imul
istore 7
iload 4
iload 7
iadd
istore 8
iload 8
istore 2
iload 0
istore 9
iload 1
istore 10
iload 9
iload 10
if_icmplt true11
ldc 0
goto cmp_end11
true11:
ldc 1
cmp_end11:
istore 11
iload 11
ldc 0
if_icmpeq if_0
ldc "xablau\n"
astore 12
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 12
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
goto end_else_0
if_0:
ldc "n entrou\n"
astore 13
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 13
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
end_else_0:
iload 2
istore 14
iload 0
istore 15
iload 14
iload 15
if_icmpgt true16
ldc 0
goto cmp_end16
true16:
ldc 1
cmp_end16:
istore 16
iload 2
istore 17
iload 1
istore 18
iload 17
iload 18
if_icmpgt true19
ldc 0
goto cmp_end19
true19:
ldc 1
cmp_end19:
istore 19
iload 16
iload 19
ior
istore 20
iload 20
ldc 0
if_icmpeq if_2
ldc "entrou aq\n"
astore 21
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 21
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
goto end_else_2
if_2:
ldc "oloco meu\n"
astore 22
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 22
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
end_else_2:
ldc 0
istore 0
test_for0:
iload 0
istore 23
ldc 10
istore 24
iload 23
iload 24
if_icmplt true25
ldc 0
goto cmp_end25
true25:
ldc 1
cmp_end25:
istore 25
ldc "segura muleq\n"
astore 26
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 26
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
iload 25
ldc 1
if_icmpeq check_incremento_0
goto exit_for_0
check_incremento_0:
iinc 0 +1
goto test_for0
exit_for_0:
ldc 0
istore 27
iload 27
istore 0
ldc 0
istore 28
iload 28
istore 1
enter_while1:
iload 0
istore 30
ldc 10
istore 31
iload 30
iload 31
if_icmplt true32
ldc 0
goto cmp_end32
true32:
ldc 1
cmp_end32:
istore 32
iload 1
istore 33
ldc 10
istore 34
iload 33
iload 34
if_icmplt true35
ldc 0
goto cmp_end35
true35:
ldc 1
cmp_end35:
istore 35
iload 32
iload 35
ior
istore 36
iload 36
ldc 1
if_icmpne break1
ldc "xama\n"
astore 37
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 37
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
iload 0
istore 38
ldc 2
istore 39
iload 38
iload 39
iadd
istore 40
iload 40
istore 0
iload 1
istore 41
ldc 1
istore 42
iload 41
iload 42
iadd
istore 43
iload 43
istore 1
goto enter_while1
break1:
return
.end method
