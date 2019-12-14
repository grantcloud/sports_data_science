# common helper functions

def vis_null(df):
    sns.heatmap(df.isnull(), cbar=False, cmap="YlGnBu_r")
    plt.show()