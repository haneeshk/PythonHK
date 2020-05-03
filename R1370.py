# %% codecell

import sys
import os
from os.path import dirname
sys.path.append(os.getcwd()+"/startup")
from IPython.display import display as Echo
from initHK import *

# %% markdown

The standard deformation mapping is as follows

$$
\begin{align}
\usf{x}(\usf{X},\tau)&=\usf{R}(\tau)\usf{X}+\usf{c}(\tau)\\
\usf{V}(\usf{X},\tau)&=\usf{R}'(\tau)\usf{X}+\usf{c}'(\tau)
\end{align}
$$

The above equations in the lagrangian description is
$$
\begin{align}
\usf{v}(\usf{x},\tau)&=\usf{W}(\tau)\pr{\usf{x}-\usf{c}(\tau)}+\usf{c}'(\tau)\\
\usf{X}(\usf{x},\tau)&=\usf{R}^{\sf T}(\tau)\pr{\usf{x}-\usf{c}(\tau)}
\end{align}
$$
 If $\usf{c}'(\tau)$ is $\usf{0}$, i.e., $\usf{c}(\tau)=\usf{c}_0$. Then the material particle located at $\usf{c}_0$ does not move.


$\usf{c}(\tau)$
Is there a point (marterial particle) where that does not move?///////



# %%latex

I am good
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
