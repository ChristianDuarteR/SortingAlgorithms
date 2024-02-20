import matplotlib

import executing_time_gathering
import matplotlib.pyplot as plot
matplotlib.use('TkAgg')
import pandas as pd

if __name__ == "__main__":
    minimum_size = 10000
    maximum_size = 30000
    step = 5000
    samples_by_size = 7

    table = executing_time_gathering.take_execution_time(minimum_size, maximum_size, step, samples_by_size)
    df = pd.DataFrame(table,
                      columns=["Size", "Quick Sort",
                               "Merge Sort", "Insertion Sort"])
    print(df)

    df.plot(x="Size",
            y=["Quick Sort", "Merge Sort", "Insertion Sort"], kind="line", marker="o")

    plot.plot(df)
    plot.show()


