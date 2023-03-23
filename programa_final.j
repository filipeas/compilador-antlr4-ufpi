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
fload 2
fstore 19
ldc "\n"
astore 20
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 19
invokevirtual java/io/PrintStream/print(F)V
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 20
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
iload 0
istore 21
iload 1
istore 22
iload 21
iload 22
iadd
istore 23
ldc 2.0
fstore 24
iload 23
i2f
fstore 23
fload 23
fload 24
fdiv
fstore 25
fload 25
fstore 2
ldc "Resultado: "
astore 26
fload 2
fstore 27
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 26
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 27
invokevirtual java/io/PrintStream/print(F)V
return
.end method
.method public static media(FF)F
.limit stack 5
.limit locals 300
ldc 0.0
fstore 31
fload 0
fstore 32
fload 1
fstore 33
fload 32
fload 33
fadd
fstore 34
ldc 2
istore 35
iload 35
i2f
fstore 35
fload 34
fload 35
fdiv
fstore 36
fload 36
fstore 31
fload 31
fstore 37
fload 37
freturn
return
.end method
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 0.0
fstore 38
ldc 0.0
fstore 39
bipush 0
istore 40
bipush 0
istore 41
ldc "Programa Fatorial. Digite o numero?"
astore 42
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 42
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
istore 43
iload 43
invokestatic programa_final.fatorial(I)I
istore 4
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 4
invokevirtual java/io/PrintStream/print(I)V
ldc "Programa media. Digite os valores?"
astore 44
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 44
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
istore 45
getstatic programa_final/n2 I
istore 46
getstatic programa_final/m F
fstore 47
iload 45
iload 46
fload 47
invokestatic programa_final.mostrarMedia(IIF)V
ldc "Programa media v2. Digite os valores?"
astore 48
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 48
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 38
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 39
ldc "media calculada"
astore 49
fload 38
fstore 50
fload 39
fstore 51
fload 50
fload 51
invokestatic programa_final.media(FF)F
fstore 28
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 49
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 28
invokevirtual java/io/PrintStream/print(F)V
return
.end method
