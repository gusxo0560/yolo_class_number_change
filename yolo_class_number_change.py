import os

data_dir = ['Dendrolimus spectabilis','Rhyacionia duplana', 'Monochamus alternatus']

for data_num, data in enumerate(data_dir):
    path_dir = './' + data + '/'

    file_list = [os.path.join(path_dir, _) for _ in os.listdir(path_dir) if _.endswith(".txt")];

    output_path = './output/' + data
    print(file_list)
    for num, i in enumerate(file_list):

        txt_open_ =  open(i, 'r')
        new_txt = open(output_path + '/' + i.split("/")[-1:][0], 'w')

        while True:
            line = txt_open_.readline()
            if not line:
                break
            x = line.split(" ")[1:][0]
            y = line.split(" ")[1:][1]
            w = line.split(" ")[1:][2]
            h = line.split(" ")[1:][3]
            new_txt.write(str(data_num) + " " + x + " " + y + " " + w + " " + h + '\n')


        new_txt.close()

        txt_open_.close()


