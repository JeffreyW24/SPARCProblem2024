import random
import matplotlib.pyplot as plt

def picksmall(queue): #this strategy picks the small baskets first until the queue is all large baskets
    if len(queue) == 0:
        return 2
    if all(element == 0 for element in queue):
        return 0
    if all(element == 1 for element in queue):
        return 1
    else:
        return 0

def lastComeLastServe(queue): #this strategy picks the last person in the queue
    if len(queue) == 0:
        return 2
    
    return queue[len(queue)-1]

def picklarge(queue): #this strategy picks the large baskets first
    if len(queue) == 0:
        return 2
    if all(element == 0 for element in queue):
        return 0
    if all(element == 1 for element in queue):
        return 1
    else:
        return 1

def firstComeFirstServe(queue): #this strategy is what current queues do
    if len(queue) == 0:
        return 2
    return queue[0]

def run_simulation(strategy_func, limit):
    queue = [] #queue starts empty
    time = 1 #this counter tracks time (each unit is 30 seconds)
    processed = 0 #counts how many customers have been processed
    processing = 0 #used to keep track of if the cashier is processing a customer

    while time <= limit: #simulates time
        if time % 2 == 0: #adds a customer to the queue
            temp = random.randint(1, 10)
            if temp == 1:
                queue.append(1)
            else:
                queue.append(0)

        if processing == 0: #if not busy
            current_customer = strategy_func(queue) #uses one of the above strategies

            if current_customer == 0:
                queue.remove(0)
                processed += 1
            elif current_customer == 1:
                processing = 10
                queue.remove(1)
            else:
                pass

        if processing != 0: #if processing a large basket, decreases the remaining time
            processing -= 1
            if processing == 0:
                processed += 1

        time += 1

    return processed

def run_multiple_simulations(strategy_func, num_simulations, limit):
    results = []
    for _ in range(num_simulations):
        results.append(run_simulation(strategy_func, limit))
    return results

def plot_results(results_small, results_lcls, results_large, results_fcfs):
    plt.plot(results_small, label='picksmall()', marker='o')
    plt.plot(results_lcls, label='lastComeLastServe()', marker='o')
    plt.plot(results_large, label='picklarge()', marker='o')
    plt.plot(results_fcfs, label='firstComeFirstServe()', marker='o')
    plt.title('Simulation Results')
    plt.xlabel('Simulation')
    plt.ylabel('Customers Processed')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    num_simulations = 100 #number of simulations
    limit = 20000 #amount of time during simulations

    results_small = run_multiple_simulations(picksmall, num_simulations, limit)
    results_lcls = run_multiple_simulations(lastComeLastServe, num_simulations, limit)
    results_large = run_multiple_simulations(picklarge, num_simulations, limit)
    results_fcfs = run_multiple_simulations(firstComeFirstServe, num_simulations, limit)

    plot_results(results_small, results_lcls, results_large, results_fcfs)
