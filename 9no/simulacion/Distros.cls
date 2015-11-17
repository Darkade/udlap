VERSION 1.0 CLASS
BEGIN
  MultiUse = -1  'True
END
Attribute VB_Name = "distros"
Attribute VB_GlobalNameSpace = False
Attribute VB_Creatable = False
Attribute VB_PredeclaredId = False
Attribute VB_Exposed = False

Public Function Geometrica(p As Double)
Geometrica = Int(Log(Rnd()) / Log(1 - p)) + 1
End Function

Public Function Exponencial(lambda As Double)
Exponencial = -1 / lambda * Log(Rnd())
End Function

Public Function Poisson(lambda As Long)
u = Rnd()
pr = Exp(-1 * lambda)
F = pr
X = 0

Do While u > F
   pr = lambda * pr / (X + 1)
   F = F + pr
   X = X + 1
Loop

Poisson = X
End Function
Public Function Box_Muller()
'Genera dos normales cero uno
Pi = WorksheetFunction.Pi()
r = Sqr(Exponencial(0.5))
t = 2 * Pi * Rnd()
Box_Muller = Array(r * Cos(t), r * Sin(t))
End Function


Public Function Obs_Geometrica(p As Double, m As Long)
Dim arreglo()
ReDim arreglo(1 To m)
For i = 1 To m
    arreglo(i) = Geometrica(p)
Next

Obs_Geometrica = arreglo
End Function

Public Function Obs_Exponencial(lambda As Double, m As Long)
Dim arreglo()
ReDim arreglo(1 To m)
For i = 1 To m
    arreglo(i) = Exponencial(lambda)
Next
Obs_Exponencial = arreglo
End Function

Public Function Obs_Poisson(lambda As Long, m As Long)
Dim arreglo()
ReDim arreglo(1 To m)
For i = 1 To m
    arreglo(i) = Poisson(lambda)
Next
Obs_Poisson = arreglo
End Function

Public Function Obs_Box_Muller(m As Long)
Dim arreglo()
ReDim arreglo(1 To m, 1 To 2)
For i = 1 To m
    resultado = Box_Muller()
    arreglo(i, 1) = resultado(0)
    arreglo(i, 2) = resultado(1)
Next
Obs_Box_Muller = arreglo
End Function

