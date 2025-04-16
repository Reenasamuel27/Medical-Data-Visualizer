# This entrypoint file to be used in development. Start by reading README.md
import medical_data_visualizer
from unittest import main
from medical_data_visualizer import draw_cat_plot, draw_heat_map
 
draw_cat_plot().savefig('catplot.png')
draw_heat_map().savefig('heatmap.png')

# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)
