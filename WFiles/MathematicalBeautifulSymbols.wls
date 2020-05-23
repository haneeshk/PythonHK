(* For Atom, use soft wrap *)
$SessionID
SS=Framed[Style[#,FontColor->White],Background->Black,FrameMargins->{{20,20},{30,30}},ImageMargins-> 0,Frame -> True, FrameStyle->Directive[Black, 25]] &;
D[Sin[p]^2,p]//SS
D[Sin[p]^2,p]//TraditionalForm//SS
pi=\[Pi];
Plot[Sin[10 x],{x,-pi,pi}]//SS
Get["/Users/haneeshkesari/Downloads/MaTeX/MaTeX/MaTeX.m"];
Format[jNi]:=MaTeX["{\\color{white} ^j\!\\boldsymbol{N}_i}",Preamble->{"\\usepackage{color}"}];
jNi//SS
RotationMatrix[jNi ,{1,1,1}]//MatrixForm//SS
Expand@((1+jNi)^10)//TraditionalForm//SS
D[Sin[अ]^2,अ]//SS

Format[x]:=Subscript[ई,ε]
x//SS
Prime/@Range[10]
N[#^2+Sin[#]] & /@ Range[0,1,0.1]
2+2
