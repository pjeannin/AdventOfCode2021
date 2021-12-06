
#include <vector>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>

std::vector<int> convert_to_vector(std::string str)
{
    std::vector<int> vec;
    std::stringstream ss(str);
    int i;
    while (ss >> i)
    {
        vec.push_back(i);
        if (ss.peek() == ',')
            ss.ignore();
    }
    return vec;
}

std::string read_file(std::string filename)
{
    std::ifstream file(filename);
    std::stringstream ss;
    ss << file.rdbuf();
    return ss.str();
}

int main(int ac, char **av) {
    std::vector<int> data = convert_to_vector(read_file("inputFile.txt"));
    for (int _ = 0; _ < 256; ++_) {
    std::cout << _ << std::endl;
    std::cout << data.size() << std::endl;
    long long size = data.size();
        for (int j = 0; j < size; ++j) {
            data[j] -= 1;
            if (data[j] < 0) {
                data[j] = 6;
                data.push_back(8);
            }
        }
    }



    std::cout << data.size() << std::endl;

    return (0);
}