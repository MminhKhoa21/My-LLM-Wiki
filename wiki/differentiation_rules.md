---
type: concept
title: "Differentiation Rules"
description: "Mathematical rules used to compute derivatives of algebraic functions."
tags: [calculus, mathematics, derivative, rules]
timestamp: 2026-07-05
sources: ["raw/calculus_derivatives.txt"]
---

# Differentiation Rules

Calculating derivatives using the limit definition can be tedious. Instead, we use a set of algebraic rules to compute the [[derivative]] of more complex functions.

## Basic Rules

Let \(c\) be a constant, and \(f(x)\) and \(g(x)\) be differentiable functions.

### 1. Constant Rule
The derivative of a constant function is zero:
\[\frac{d}{dx}(c) = 0\]

### 2. Power Rule
For any real number \(n\):
\[\frac{d}{dx}(x^n) = n x^{n-1}\]

### 3. Sum Rule
The derivative of a sum is the sum of the derivatives:
\[\frac{d}{dx}(f(x) + g(x)) = f'(x) + g'(x)\]

### 4. Product Rule
The derivative of the product of two functions:
\[\frac{d}{dx}(f(x) \cdot g(x)) = f'(x)g(x) + f(x)g'(x)\]

### 5. Chain Rule
The derivative of a composite function:
\[\frac{d}{dx}(f(g(x))) = f'(g(x)) \cdot g'(x)\]

## Applications
These rules allow for the systematic differentiation of polynomials, rational functions, and other composite functions. They form the foundation of computational techniques in calculus, popularized using notation developed by [[gottfried_leibniz]].
