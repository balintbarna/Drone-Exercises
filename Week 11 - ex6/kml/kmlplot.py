try:
    from kml.exportkml import kmlclass  # "app" case
except:
    from exportkml import kmlclass                   # "__main__" case

def kml_color(val):
    # color: red,green,blue,cyan,yellow,grey,red_poly,yellow_poly,green_poly
    if val <= 0.5:
        return 'red'
    if val <= 0.7:
        return 'green'
    
def plot_kml(input_path, output_path):
    print("plotting kml from " + input_path)
    # altitude: use 'absolute' or 'relativeToGround'
    f = open(input_path,'r')

    line = f.readline().split("\n")[0].split("\t")
    kml = kmlclass()
    kml.begin(output_path+'.kml', 'Example', 'Example on the use of kmlclass', 0.7)
    while True:
        pLine = line
        line = f.readline().split("\n")[0].split("\t")
        if '' == line[0]:
            break
        if float(pLine[1]) != 0.0 and pLine[2] != 0.0:
            kml.trksegbegin ('', '', kml_color(0), 'absolute')
            kml.pt(float(pLine[1]), float(pLine[2]), 0.0)
            kml.pt(float(line[1]), float(line[2]), 0.0)
            kml.trksegend()
    kml.end()
    print("plotting finished in " + output_path)

if __name__ == "__main__":
    # test functions
    plot_kml("Week 11 - ex6/input/gps_data_1583748176.57617.txt", "Week 11 - ex6/output/track1")
    plot_kml("Week 11 - ex6/input/gps_data_1583749050.86728.txt", "Week 11 - ex6/output/track2")