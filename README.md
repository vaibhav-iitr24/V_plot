At first that mapped.bed.gz file unziped and running the second command(refer vpt.sh) to convert "fragment position" value in the range value. 
Also we extracted that value with "fragment size", separated by tab & sorted. And stored in op.tsv. 
In third command(refer vpt.sh) we obtained frequency of pair(fragment position vs fragment size) stored in another file(file.tsv) by required format.
Now python file created(plot1.py). Written required script to generate V-plot. For reading and accessing data pandas used while for plotting matplotlib library used.
By running last command (refer vpt.sh) you can see the plot.
