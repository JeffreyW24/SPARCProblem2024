import random
import matplotlib.pyplot as plt


def picksmall(queue):
    if len(queue) == 0:
        return 2
    if all(element == 0 for element in queue):
        return 0
    if all(element == 1 for element in queue):
        return 1
    else:
        return 0


def lastComeLastServe(queue):
    if len(queue) == 0:
        return 2

    return queue[len(queue) - 1]


def picklarge(queue):
    if len(queue) == 0:
        return 2
    if all(element == 0 for element in queue):
        return 0
    if all(element == 1 for element in queue):
        return 1
    else:
        return 1


def firstComeFirstServe(queue):
    if len(queue) == 0:
        return 2
    return queue[0]


def run_simulation(strategy_func, limit):
    queue = []
    time = 1
    processed = 0
    processing = 0

    while time <= limit:
        if time % 2 == 0:
            temp = random.randint(1, 10)
            if temp == 1:
                queue.append(1)
            else:
                queue.append(0)

        if processing == 0:
            current_customer = strategy_func(queue)

            if current_customer == 0:
                queue.remove(0)
                processed += 1
            elif current_customer == 1:
                processing = 10
                queue.remove(1)
            else:
                pass

        if processing != 0:
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


def plot_results(results_small, results_lcls):
    plt.plot(results_small, label='picksmall()', marker='o')
    plt.plot(results_lcls, label='lastComeLastServe()', marker='o')
    plt.title('Simulation Results')
    plt.xlabel('Simulation')
    plt.ylabel('Customers Processed')
    plt.legend()
    plt.show()


if __name__ == "__main__":
    num_simulations = 100
    limit = 80000

    results_small = run_multiple_simulations(picksmall, num_simulations, limit)
    results_lcls = run_multiple_simulations(lastComeLastServe, num_simulations, limit)

    plot_results(results_small, results_lcls)
