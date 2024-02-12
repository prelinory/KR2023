from django.shortcuts import render, redirect
from .forms import *
import numpy as np
from .models import *
from django.core.exceptions import ValidationError


# Решение СЛАУ методом итераций
def iter(a, y, x0, epsilon, max_iter):
    n = len(a)
    res = x0.copy()

    iterations = 0
    while iterations < max_iter:
        iterations += 1
        Xn = np.zeros(n, dtype=int)
        for i in range(n):
            Xn[i] = y[i] / a[i][i]
            for j in range(n):
                if i == j:
                    continue
                else:
                    Xn[i] -= round(a[i][j] / a[i][i] * res[j])

        if np.max(np.abs(Xn - res)) < epsilon:
            break

        res = Xn.copy()

    return res, iterations


def input_one(request):
    if request.method == "POST":
        form = EquationForm(request.POST)
        if form.is_valid():
            n = form.cleaned_data["n"]
            return redirect("input_two", n=n)

    else:
        form = EquationForm()
    return render(request, "main/index.html", {"form": form})


def input_two(request, n):
    my_error = False
    if request.method == "POST":
        a = np.zeros((n, n), dtype=int)
        z = np.zeros((n, n + 1), dtype=int)
        y = np.zeros(n, dtype=int)
        form = EquationFormTwo(n, request.POST)
        if form.is_valid():
            for x in range(0, n):
                temp_name_x = f"Коэффициент x[{x+1}][{x+1}]"
                temp_coefficient_x = int(form.cleaned_data[temp_name_x])
                temp_sum = 0
                for j in range(0, n):
                    field_name_x = f"Коэффициент x[{x+1}][{j+1}]"
                    coefficient_x = int(form.cleaned_data[field_name_x])
                    a[x][j] = coefficient_x
                    z[x][j] = coefficient_x
                    if j != x:
                        temp_sum += coefficient_x
                if abs(temp_sum) > abs(temp_coefficient_x):
                    my_error = True
                field_name_y = f"Свободный член y[{x+1}]"
                coefficient_y = int(form.cleaned_data[field_name_y])
                y[x] = coefficient_y

                z[x][j + 1] = coefficient_y

            x0 = []
            for x in range(0, n):
                field_name_initial = f"Начальное приближение x[{x+1}]"
                initial_value = int(form.cleaned_data[field_name_initial])
                x0.append(initial_value)

            epsilon = float(form.cleaned_data["Точность"])
            max_iter = int(form.cleaned_data["Максимальное число итераций"])

            print("Система уравнений:")
            for i in range(n):
                for j in range(n + 1):
                    if j != n:
                        print(a[i][j], end="\t")

                    else:
                        print(y[i], end="\t")
                print()
            print(y)
            x, iterations = iter(a, y, x0, epsilon, max_iter)

            print("Решение системы уравнений:")
            for i in range(n):
                print(f"x[{i}] = {x[i]}")

            print("Количество итераций:", iterations)
            equation = Equation(n=n, a=z, y=x, iterations=iterations, x=x0)
            equation.save()

        return render(
            request,
            "main/input_two.html",
            {
                "iterations": iterations,
                "x": x,
                "y": y,
                "a": a,
                "n": n,
                "my_error": my_error,
            },
        )
    else:
        form = EquationFormTwo(n)
    return render(request, "main/input_two.html", {"form": form, "my_error": my_error})
