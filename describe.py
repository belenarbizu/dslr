import sys
import pandas as pd

class DataAnalysis:

    def __init__(self):
        self.data_dict = []
        self.num_data = []

    def count(self, col_num):
        len(col_num)
    
    def mean(self, col_num):
        pass
    
    def min(self, col_num):
        min_num = col_num[0]
        for i in range(len(col_num)):
            if col_num[i] < min_num:
                min_num = col_num[i]
    
    def max(self, col_num):
        max_num = col_num[0]
        for i in range(len(col_num)):
            if col_num[i] > max_num:
                max_num = col_num[i]
    
    def std(self, col_num):
        pass
    
    def quartile(self, col_num):
        pass

    def read_file(self, dataset):
        try:
            self.data_dict = pd.read_csv(dataset, index_col="Index")
            columns_name = []
            for name in self.data_dict.columns.values:
                if isinstance(self.data_dict[name].iloc[0], int) or isinstance(self.data_dict[name].iloc[0], float):
                    columns_name.append(name)
            self.num_data = self.data_dict.loc[:, columns_name]
        except:
            print("Coludn't read the dataset")
            sys.exit(1)


def main():
    if (len(sys.argv) < 2):
        print("Usage: python3 ./describe.py dataset_name")
        sys.exit(1)

    data = DataAnalysis()
    data.read_file(sys.argv[1])

if __name__ == "__main__":
    main()