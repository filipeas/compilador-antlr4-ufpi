.class public programa_final
.super java/lang/Object
.field public static numero I
.method public static fatorial(I)I
.limit stack 5
.limit locals 300
iload 0
istore 3
ldc 1
istore 4
iload 3
iload 4
if_icmpgt true5
ldc 0
goto cmp_end5
true5:
ldc 1
cmp_end5:
istore 5
iload 5
ldc 0
if_icmpeq if_0
iload 0
istore 6
iload 0
istore 7
ldc 1
istore 8
iload 7
iload 8
isub
istore 9
iload 9
invokestatic programa_final.fatorial(I)I
istore 1
iload 6
iload 1
imul
istore 10
iload 10
ireturn
goto end_else_0
if_0:
ldc 1
istore 11
iload 11
ireturn
end_else_0:
return
.end method
.method public static mostrarMedia(FFF)V
.limit stack 5
.limit locals 300
fload 0
fstore 16
fload 1
fstore 17
fload 16
fload 17
fadd
fstore 18
ldc 2
istore 19
iload 19
i2f
fstore 19
fload 18
fload 19
fdiv
fstore 20
fload 20
fstore 2
ldc "Resultado: "
astore 21
fload 2
fstore 22
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 21
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 22
invokevirtual java/io/PrintStream/print(F)V
return
.end method
.method public static media(FF)F
.limit stack 5
.limit locals 300
ldc 0.0
fstore 26
fload 0
fstore 27
fload 1
fstore 28
fload 27
fload 28
fadd
fstore 29
ldc 2
istore 30
iload 30
i2f
fstore 30
fload 29
fload 30
fdiv
fstore 31
fload 31
fstore 26
fload 26
fstore 32
fload 32
freturn
return
.end method
.method public static main([Ljava/lang/String;)V
.limit stack 10
.limit locals 300
ldc 0.0
fstore 33
ldc 0.0
fstore 34
ldc 0.0
fstore 35
ldc "Programa Fatorial. Digite o numero?"
astore 36
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 36
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextInt()I
istore 0
iload 0
istore 37
iload 37
invokestatic programa_final.fatorial(I)I
istore 1
getstatic java/lang/System/out Ljava/io/PrintStream;
iload 1
invokevirtual java/io/PrintStream/print(I)V
ldc "Programa media. Digite os valores?"
astore 38
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 38
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 33
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 34
fload 33
fstore 39
fload 34
fstore 40
fload 35
fstore 41
fload 39
fload 40
fload 41
invokestatic programa_final.mostrarMedia(FFF)V
ldc "Programa media v2. Digite os valores?"
astore 42
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 42
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 33
new java/util/Scanner
dup
getstatic java/lang/System/in Ljava/io/InputStream;
invokespecial java/util/Scanner/<init>(Ljava/io/InputStream;)V
invokevirtual java/util/Scanner/nextFloat()F
fstore 34
ldc "media calculada"
astore 43
fload 33
fstore 44
fload 34
fstore 45
fload 44
fload 45
invokestatic programa_final.media(FF)F
fstore 23
getstatic java/lang/System/out Ljava/io/PrintStream;
aload 43
invokevirtual java/io/PrintStream/print(Ljava/lang/String;)V
getstatic java/lang/System/out Ljava/io/PrintStream;
fload 23
invokevirtual java/io/PrintStream/print(F)V
return
.end method
