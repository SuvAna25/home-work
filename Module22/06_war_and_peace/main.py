import collections
import zipfile


def upzip(archive):
    zfile = zipfile.ZipFile(archive, 'r')
    for i_file_name in zfile.namelist():
        zfile.extract(i_file_name)
    zfile.close()


def collect_stats(file_name):
    result = {}
    if file_name.endswith('.zip'):
        upzip(file_name)
        file_name = ''.join((file_name[:-3], 'txt'))
    text_file = open(file_name, 'r', encoding='utf-8')
    for i_line in text_file:
        for i_char in i_line:
            if i_char.isalpha():
                if i_char not in result:
                    result[i_char] = 0
                result[i_char] += 1
    text_file.close()
    return result


def print_stats(stats):
    print("+{:-^19}+".format('+'))
    print("|{:^9}|{:^9}|".format('Буква', 'Частота'))
    print("+{:-^19}+".format('+'))
    for char, count in stats.items():
        print("|{:^9}|{:^9}|".format(char, count))
    print("+{:-^19}+".format('+'))


def sort_by_frequency(stats_dict):
    sorted_values = sorted(stats_dict.values(), reverse=True)
    sorted_dict = collections.OrderedDict()
    for i_values in sorted_values:
        for i_key in stats_dict.keys():
            if stats_dict[i_key] == i_values:
                sorted_dict[i_key] = stats_dict[i_key]

    return sorted_dict


file_name = 'voyna-i-mir.zip'
stats = collect_stats(file_name)
stats = sort_by_frequency(stats)
print_stats(stats)
