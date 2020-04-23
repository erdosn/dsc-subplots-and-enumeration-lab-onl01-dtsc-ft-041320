import matplotlib.pyplot as plt


def plot_histogram(df, country_name, add_grid=True,
                   alpha=0.8, color="#eb34d5"):
    """
    this function is built to plot histograms for 
    individual countries from the population dataframe
    
    inputs
    df = pandas dataframe
    country name = name of country from dataframe
    add_grid = option to turn off/on grid on plot
    alpha = alpha value of histogram
    color = default pink, color of histogram bars
    
    
    returns nothing
    plots histogram
    """
    sub_df = df.loc[df["Country Name"]==country_name]
    plt.figure(figsize=(8, 5))
    if add_grid:
        plt.grid(zorder=0)
    plt.hist(sub_df["Value"], bins=20, label="Value", 
             zorder=2, alpha=alpha, color=color,
             edgecolor="k", linewidth=3)
    plt.legend()
    plt.title(country_name)
    plt.show()
    
    
