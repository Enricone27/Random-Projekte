Attribute VB_Name = "Modul3"
Sub zahlensortieren()
Dim x, y As Integer
 x = Int(Rnd() * 100 + 1)
 y = Int(Rnd() * 100 + 1)
 Z = Int(Rnd() * 100 + 1)

 MsgBox (Str(x) + ";" + Str(y) + ";" + Str(y))
 
 If y > x Then
    MsgBox (Str(y) + ";" + Str(x))
    
 Else
    MsgBox (Str(x) + ";" + Str(y))
 End If
 
End Sub

Sub zahlensortieren1()
Dim x(10), min(10), mina As Integer
Dim ausgabe As String

For i = 1 To 10
    x(i) = Int(Rnd() * 100 + 1)
    Next i

ausgabe = ""

For i = 1 To 10
	ausgabe = ausgabe + Str(x(i)) + " "
	Next i
		
MsgBox (ausgabe)
 
min(1) = x(1)
 
For ii = 1 To 10
	mina = 100
	For i = 1 To 10   
		If x(i) > min(ii - 1) Then
            If x(i) <= mina Then
				min(ii) = x(i)
                mina = x(i)
                End If
        End If
       
		Next i

	Next ii

ausgabe = ausgabe + Chr(13)

For i = 1 To 10
    ausgabe = ausgabe + Str(min(i)) + " "
    Next i

MsgBox (ausgabe)

End Sub
