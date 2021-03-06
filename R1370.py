# %% codecell

import sys
import os
from os.path import dirname
sys.path.append(os.getcwd()+"/startup")
from IPython.display import display as Echo
from initHK import *

# %% markdown
### The material particle that does not move.
The standard deformation mapping is as follows


$$
\begin{align}
\usf{x}(\usf{X},\tau)&=\usf{R}(\tau)\usf{X}+\usf{c}(\tau)\\
\usf{V}(\usf{X},\tau)&=\usf{R}'(\tau)\usf{X}+\usf{c}'(\tau)
\end{align}
$$

The above equations in the eulerian description is
$$
\begin{align}
\usf{v}(\usf{x},\tau)&=\usf{W}(\tau)\pr{\usf{x}-\usf{c}(\tau)}+\usf{c}'(\tau)\\
\usf{X}(\usf{x},\tau)&=\usf{R}^{\sf T}(\tau)\pr{\usf{x}-\usf{c}(\tau)}
\end{align}
$$

Is there a point (marterial particle) where that does not move?



# %%markdown
#### $\usf{c}'(\tau)=\usf{0}$ is a sufficient condition for there to exist a material particle that does not move. (True)
Let us consider the case $\usf{c}'(\tau)$ is $\usf{0}$, i.e., $\usf{c}(\tau)=\usf{c}_0$.
$$
\begin{align}
\usf{x}(\usf{X},\tau)&=\usf{R}(\tau)\pr{\usf{X}+\usf{R}^{\sf T}(\tau)\usf{c}_0}\\
\usf{V}(\usf{X},\tau)&=\usf{R}'(\tau)\usf{X}\\
\usf{v}(\usf{x},\tau)&=\usf{W}(\tau)\pr{\usf{x}-\usf{c}_0}\\
\usf{X}(\usf{x},\tau)&=\usf{R}^{\sf T}(\tau)\pr{\usf{x}-\usf{c}_0}
\end{align}
$$

From the eulerian velocity field we get that the material particle located at the spatial point $\usf{c}_0$ does not move. From the eulerian version of the deformation mapping we have that the spatial point $\usf{c}_0$ is occupied by the material particle $\usf{0}$.

Let's see if we get the same result from the Lagrangian description. From the Lagrangian velocity field we have that the material particle $\usf{0}$ always has zero velocity. Using this information in the Lagrangian deformation mapping we get that the material particle $\usf{0}$ is always located at $\usf{c}_0$.

From the discussion in this section we can say that $\usf{c}'(\tau)=\usf{0}$ is a sufficient condition for there to exist material particle that does not move.

# %%markdown

####  $\usf{c}'(\tau)=\usf{0}$ is a necessary condition for there to exist a material particle that does not move (ans: False)

Consider the cases when if $\usf{R}$ is presribed then $\usf{c}$ is constructed as
$$
\begin{equation}
\usf{c}(\tau)=\pr{\usf{I}-\usf{R}(\tau)}\usf{C}_0,
\end{equation}
$$
where $\usf{C}_0$ is an arbitrary constant vector.

Clearly, $\usf{c}'(\tau)\neq=\usf{0}$, since it is equal to $-\usf{R}'(\tau)\usf{C}_0$. However, it can be shown that the materials particle $\usf{C}_0$ always has zero velocity, i.e., it does not move. Thus, $\usf{c}'(\tau)=0$ is not a necessary condition for there to exist a materials particle that does not move.



# %%markdown

#### If $\usf{c}'(\tau)\neq \usf{0}$ then there does not  exist a material particle that does not move. (ans False)

The statement is the contrapositive of the previous claim.






# %%markdown
#### So, what is a necessary condition for there to exist a point that does not move?

A necessary and sufficient condition condition  that there exists a point $\usf{X}_0$ that does not move is that there exist a pont $\usf{X}$ such that

$$
(\usf{I}-\usf{R}(\tau))\usf{X}=\usf{c}(\tau)
$$
for all $\tau$.










# %%codecell
data={'Name':["x","y","z"],'value':[1.0,2.0,3.0]}
import pandas as pd
data=pd.DataFrame(data)
display(data)
cos*ov*sin-at-pi/2;
# %% markdown

$$
\newcommand{\forcemag}{f}
\newcommand{\physF}{\boldsymbol{\mathfrak{f}}}
\newcommand{\physB}{\mathscr{b}} % Width of the thin film
\newcommand{\physE}{{\mathpzc{E}}} % Young's modulus of the thin film
\newcommand{\physh}{\mathscr{h}} % Thickness of the thin film.
\newcommand{\physe}{\mathbscr{e}} % Thickness of the thin film.
\newcommand{\physf}{\boldsymbol{\mathfrak{f}}} % Thickness of the thin film.
\newcommand{\physm}{\mathscr{m}}
\newcommand{\physu}{\mathbscr{u}}
\newcommand{\physw}{\mathscr{w}}
\newcommand{\rtple}[1]{\boldsymbol{#1}}
\renewcommand{\u}[1]{\boldsymbol{#1}}
\newcommand{\OriginRefEucldPtSpace}{O_{\mathrm{ R}}}
\newcommand{\MapManifoldToRefEucldPtSpace}{\kappa_{\mathrm{ R}}}
\renewcommand{\t}[1]{\tilde{#1}}
\renewcommand{\b}[1]{\mathbb{#1}}
\renewcommand{\c}[1]{\mathcal{#1}}
\newcommand{\lsc}[2][\mathscr{l}]{{}^{ #1 }\! #2}
\newcommand{\lscH}[1]{\lsc[H]{#1}}
\newcommand{\dsf}[1]{\Delta\boldsymbol{\sf #1}}
\newcommand{\tpsb}[1]{\left. #1 \right.^{\sf T}}
\newcommand{\tps}[1]{\left( #1 \right)^{\sf T}}
\newcommand{\usf}[1]{\u{\sf #1}}
\newcommand{\busf}[1]{\bar{\usf{ #1}}}
\newcommand{\tu}[1]{\tilde{\u{ #1}}}
\newcommand{\tusf}[1]{\tilde{\usf{ #1}}}
\newcommand{\btusf}[1]{\bar{\tusf{ #1}}}
\newcommand{\pr}[1]{\left( #1 \right)}
\newcommand{\D}[1]{D\hspace{-.1em}#1}
\newcommand{\Dr}{D\hspace{-.1em}\varrho}
\newcommand{\Drp}{\Dr^{+}}
\newcommand{\Drm}{\Dr^{-}}
\newcommand{\Dro}{\dot{\rho}}
\newcommand{\DDro}{\ddot{\rho}}
\newcommand{\Df}{\dot{f}}
\newcommand{\DDf}{\ddot{f}}
\newcommand{\Drop}{\Dro^{+}}
\newcommand{\Drom}{\Dro^{-}}
\newcommand{\Dl}{\dot{l}}
\newcommand{\Da}{\dot{a}}
\newcommand{\DDl}{\ddot{l}}
\newcommand{\DF}{\dot{F}}
\newcommand{\DDF}{\ddot{F}}
\newcommand{\Dlp}{\Dl^{+}}
\newcommand{\Dlm}{\Dl^{-}}
\newcommand{\Dam}{\Da^{-}}
\newcommand{\Deq}{\mathcal{D}^{\circ}}
\newcommand{\Dst}{\mathcal{D}^{\stable}}
\newcommand{\Dnt}{\mathcal{D}^{\odot}}
\newcommand{\Dunst}{\mathcal{D}^{\otimes}}
\newcommand{\conf}{\boldsymbol{\kappa}}
\newcommand{\confp}{\tilde{\boldsymbol{\kappa}}}$$





# %%codecell


names=['John', 'James','Bill']
f@list@map(lambda x: x+' smith',names)
lase
