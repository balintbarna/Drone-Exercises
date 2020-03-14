def get_data(file):
    return file.readline().split("\n")[0].split("\t")

def write_data(file, line):
    full_text = '%02.5f\t%02.5f\t%03.5f\t%.1f\n' % (float(line[0]), float(line[1]), float(line[2]), float(line[3]))
    file.write(full_text)

def empty_line(line):
    return '' == line[0]