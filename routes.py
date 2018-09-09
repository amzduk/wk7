from server import app, valid_time
from flask import request, render_template
from Calculator import Calculator


@app.route('/', methods=['POST', 'GET'])
def interest_total():
    if request.method == 'POST':
        amountInvested = request.form['invest']
        timeInvested = request.form['time']
        interestRate = request.form['rate']
        try:
            A = float(amountInvested)
            T = float(timeInvested)
            I = float(interestRate)
        except ValueError:
            return render_template('interest_form.html', calc_total = True, 
                                    total = "error", a = amountInvested, 
                                    t = timeInvested, i = interestRate)
        if T < 0:
            return render_template('interest_form.html', calc_total = True,  
                                    a = amountInvested, t = timeInvested, 
                                    i = interestRate, calc_error = True)
        calc = Calculator(A, I)
        totalInterest = calc.total_interest(T)
        return render_template('interest_form.html', calc_total = True, 
                                total = totalInterest,  a = amountInvested, 
                                t = timeInvested, i = interestRate, 
                                calc_done = True)

    return render_template('interest_form.html', calc_total = True)


@app.route('/time', methods=['POST', 'GET'])
def time_interest():
        if request.method == 'POST':
            amountInvested = request.form['invest']
            totalInterest = request.form['total']
            interestRate = request.form['rate']
            try:
                A = float(amountInvested)
                T = float(totalInterest)
                I = float(interestRate)
            except ValueError:
                return render_template('interest_form.html', time_total = True, 
                                        total = "error", a = amountInvested, 
                                        t = timeInvested, i = interestRate)

            calc = Calculator(A, I)
            timeInvested = calc.time_required(T)
            return render_template('interest_form.html', time_total = True, 
                                    t = timeInvested,  a = amountInvested, 
                                    total = totalInterest, i = interestRate, 
                                    calc_done = True)
            

        return render_template('interest_form.html', time_total = True)


@app.route('/credits', methods=['GET'])
def credits():
    return render_template('credits.html')
