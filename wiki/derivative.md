---
type: concept
title: "The Derivative"
description: "The definition, limit formula, and geometric interpretation of the derivative."
tags: [calculus, mathematics, limit, derivative]
timestamp: 2026-07-05
sources: ["raw/calculus_derivatives.txt"]
---

# The Derivative

The **derivative** of a function measures how the function value changes as its input changes. It is the fundamental tool of differential calculus.

## Definition

For a real-valued function \(f(x)\), the derivative at a point \(x = a\) is defined as the limit:

\[f'(a) = \lim_{h \to 0} \frac{f(a + h) - f(a)}{h}\]

If this limit exists, the function \(f\) is said to be **differentiable** at \(a\).

## Properties & Interpretation

- **Instantaneous Rate of Change**: It represents how fast the dependent variable changes at a single instant.
- **Slope of Tangent**: Geometrically, \(f'(a)\) is the slope of the line tangent to the curve \(y = f(x)\) at the point \((a, f(a))\).
- **Relation to Continuity**: Differentiability at a point implies continuity at that point. However, the converse is not true; for example, \(f(x) = |x|\) is continuous but not differentiable at \(x = 0\) due to a sharp corner.

## Operations

To compute derivatives, we apply specific mathematical techniques known as [[differentiation_rules]].

## Historical Development

The mathematical formalization of derivatives is credited to [[isaac_newton]] and [[gottfried_leibniz]] in the late 17th century.
