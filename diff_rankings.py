import pandas as pd
import subprocess
import os



def run_scrapy_spiders(spider_name, output_filename):
    # Set the directory where scrapy.cfg is located (the root of the Scrapy project)
    project_root = "D:/GitHub/NBA-Overperformers/overperformers"
    output_path = f"{project_root}/overperformers/{output_filename}.csv"
    
    if os.path.exists(output_path):
        os.remove(output_path)
    
    try:
        # Change the working directory to the project root
        os.chdir(project_root)
        
        # Run the Scrapy spider via the terminal command with output file
        subprocess.run(['scrapy', 'crawl', spider_name, '-o', output_path], check=True)
        print(f"Successfully ran spider: {spider_name} and saved data to {output_path}")
    except subprocess.CalledProcessError as e:
        print(f"An error occurred while running spider: {spider_name}")
        print(e)
    except FileNotFoundError as e:
        print(f"Failed to change to the Scrapy project directory: {project_root}")
        print(e)
    return output_path


# Run your Scrapy spiders and get the path to the output files
path_to_averages = run_scrapy_spiders('averages', 'avg')
path_to_last_game = run_scrapy_spiders('last_game', 'lastgame')


season_averages = pd.read_csv(path_to_averages)
last_night_stats = pd.read_csv(path_to_last_game)

combined = pd.merge(season_averages, last_night_stats, on='Name', suffixes=('_avg', '_last'))


# Calculate the difference in each category
combined['PTS_diff'] = combined['PTS_last'] - combined['PTS_avg']
combined['AST_diff'] = combined['AST_last'] - combined['AST_avg']
combined['REB_diff'] = combined['REB_last'] - combined['REB_avg']
combined['3PM_diff'] = combined['3PM_last'] - combined['3PM_avg']

top_pts_diff = combined.nlargest(3, 'PTS_diff')[['Name', 'PTS_last', 'PTS_avg', 'PTS_diff']]
top_ast_diff = combined.nlargest(3, 'AST_diff')[['Name', 'AST_last', 'AST_avg', 'AST_diff']]
top_reb_diff = combined.nlargest(3, 'REB_diff')[['Name', 'REB_last', 'REB_avg', 'REB_diff']]
top_3pm_diff = combined.nlargest(3, '3PM_diff')[['Name', '3PM_last', '3PM_avg', '3PM_diff']]




def results():
    # Assuming you have already defined top_pts_diff, top_ast_diff, etc.
    # Convert DataFrames to HTML tables
    html_top_pts_diff = top_pts_diff.to_html(index=False, border=1)
    html_top_ast_diff = top_ast_diff.to_html(index=False, border=1)
    html_top_reb_diff = top_reb_diff.to_html(index=False, border=1)
    html_top_3pm_diff = top_3pm_diff.to_html(index=False, border=1)
    
    # Combine all HTML tables into a single HTML string with titles
    result_html = f"""
    <h3>Top 3 Points Difference:</h3>
    {html_top_pts_diff}
    <h3>Top 3 Assists Difference:</h3>
    {html_top_ast_diff}
    <h3>Top 3 Rebounds Difference:</h3>
    {html_top_reb_diff}
    <h3>Top 3 Three-Pointers Made Difference:</h3>
    {html_top_3pm_diff}
    """
    
    return result_html

