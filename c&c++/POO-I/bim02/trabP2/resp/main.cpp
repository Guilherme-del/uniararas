#include <iostream>
#include <vector>
#include <queue>
#include <stack>
#include <climits>
#include <algorithm>
#include <limits>

using namespace std;

class MetroSystem
{
private:
    struct Station
    {
        string name;
        vector<pair<int, int>> connections;
    };

    vector<Station> stations;
    vector<vector<pair<int, int>>> adjacencyList;
    vector<vector<int>> adjacencyMatrix;

public:
    void createGraph()
    {
        int numStations;
        cout << "Digite o número de estações do sistema metroviário: ";
        while (!(cin >> numStations))
        {
            cout << "Entrada inválida. Digite um número inteiro: ";
            cin.clear();
            cin.ignore(numeric_limits<streamsize>::max(), '\n');
        }

        stations.resize(numStations);
        adjacencyList.resize(numStations);
        adjacencyMatrix.resize(numStations, vector<int>(numStations, -1));

        for (int i = 0; i < numStations; i++)
        {
            cout << "Digite o nome da estação " << i << ": ";
            cin >> stations[i].name;
        }

        for (int i = 0; i < numStations; i++)
        {
            cout << "Digite as conexões da estação " << stations[i].name << ":" << endl;
            for (int j = 0; j < numStations; j++)
            {
                if (i != j)
                {
                    int weight;
                    cout << "Digite o tempo necessário para ir de " << stations[i].name << " para " << stations[j].name << ": ";
                    while (!(cin >> weight))
                    {
                        cout << "Entrada inválida. Digite um número inteiro: ";
                        cin.clear();
                        cin.ignore(numeric_limits<streamsize>::max(), '\n');
                    }

                    adjacencyList[i].push_back(make_pair(j, weight));
                    adjacencyMatrix[i][j] = weight;
                }
            }
        }

        cout << "Grafo criado com sucesso!" << endl;
    }

    void addStation()
    {
        string name;
        cout << "Digite o nome da nova estação: ";
        cin >> name;

        Station newStation;
        newStation.name = name;

        cout << "Digite as conexões da estação " << name << ":" << endl;
        for (int i = 0; i < stations.size(); i++)
        {
            if (i != stations.size() - 1)
            {
                int weight;
                cout << "Digite o tempo necessário para ir de " << name << " para " << stations[i].name << ": ";
                cin >> weight;

                newStation.connections.push_back(make_pair(i, weight));
                adjacencyList[stations.size()].push_back(make_pair(i, weight));
                adjacencyMatrix[stations.size()][i] = weight;
            }
        }

        stations.push_back(newStation);
        adjacencyList.push_back(newStation.connections);
        adjacencyMatrix.push_back(vector<int>(stations.size(), -1));

        cout << "Estação adicionada com sucesso!" << endl;
    }

    void removeStation()
    {
        string name;
        cout << "Digite o nome da estação a ser removida: ";
        cin >> name;

        auto it = find_if(stations.begin(), stations.end(), [&](const Station &station)
                          { return station.name == name; });

        if (it != stations.end())
        {
            int index = distance(stations.begin(), it);
            stations.erase(it);

            adjacencyList.erase(adjacencyList.begin() + index);
            adjacencyMatrix.erase(adjacencyMatrix.begin() + index);

            for (int i = 0; i < adjacencyList.size(); i++)
            {
                adjacencyList[i].erase(remove_if(adjacencyList[i].begin(), adjacencyList[i].end(),
                                                 [&](const pair<int, int> &connection)
                                                 {
                                                     return connection.first == index;
                                                 }),
                                       adjacencyList[i].end());
            }

            for (int i = 0; i < adjacencyMatrix.size(); i++)
            {
                adjacencyMatrix[i].erase(adjacencyMatrix[i].begin() + index);
            }

            cout << "Estação removida com sucesso!" << endl;
        }
        else
        {
            cout << "Estação não encontrada!" << endl;
        }
    }

    void breadthFirstSearch(const string &startStation)
    {
        auto it = find_if(stations.begin(), stations.end(), [&](const Station &station)
                          { return station.name == startStation; });

        if (it != stations.end())
        {
            int startIndex = distance(stations.begin(), it);
            vector<bool> visited(stations.size(), false);
            queue<int> queue;

            cout << "Busca em largura a partir da estação " << startStation << ":" << endl;

            visited[startIndex] = true;
            queue.push(startIndex);

            while (!queue.empty())
            {
                int current = queue.front();
                queue.pop();
                cout << stations[current].name << " ";

                for (const auto &connection : adjacencyList[current])
                {
                    int neighbor = connection.first;
                    if (!visited[neighbor])
                    {
                        visited[neighbor] = true;
                        queue.push(neighbor);
                    }
                }
            }

            cout << endl;
        }
        else
        {
            cout << "Estação não encontrada!" << endl;
        }
    }

    void depthFirstSearch(const string &startStation)
    {
        auto it = find_if(stations.begin(), stations.end(), [&](const Station &station)
                          { return station.name == startStation; });

        if (it != stations.end())
        {
            int startIndex = distance(stations.begin(), it);
            vector<bool> visited(stations.size(), false);
            stack<int> stack;

            cout << "Busca em profundidade a partir da estação " << startStation << ":" << endl;

            visited[startIndex] = true;
            stack.push(startIndex);

            while (!stack.empty())
            {
                int current = stack.top();
                stack.pop();
                cout << stations[current].name << " ";

                for (const auto &connection : adjacencyList[current])
                {
                    int neighbor = connection.first;
                    if (!visited[neighbor])
                    {
                        visited[neighbor] = true;
                        stack.push(neighbor);
                    }
                }
            }

            cout << endl;
        }
        else
        {
            cout << "Estação não encontrada!" << endl;
        }
    }

    void findPath(const string &startStation, const string &endStation)
    {
        auto startIt = find_if(stations.begin(), stations.end(), [&](const Station &station)
                               { return station.name == startStation; });

        auto endIt = find_if(stations.begin(), stations.end(), [&](const Station &station)
                             { return station.name == endStation; });

        if (startIt != stations.end() && endIt != stations.end())
        {
            int startIndex = distance(stations.begin(), startIt);
            int endIndex = distance(stations.begin(), endIt);

            vector<int> path;
            vector<bool> visited(stations.size(), false);
            queue<pair<int, vector<int>>> queue;

            visited[startIndex] = true;
            queue.push(make_pair(startIndex, vector<int>{startIndex}));

            while (!queue.empty())
            {
                int current = queue.front().first;
                path = queue.front().second;
                queue.pop();

                if (current == endIndex)
                {
                    cout << "Caminho encontrado entre as estações " << startStation << " e " << endStation << ":" << endl;
                    for (int stationIndex : path)
                    {
                        cout << stations[stationIndex].name << " ";
                    }
                    cout << endl;
                    return;
                }

                for (const auto &connection : adjacencyList[current])
                {
                    int neighbor = connection.first;
                    if (!visited[neighbor])
                    {
                        visited[neighbor] = true;
                        vector<int> newPath = path;
                        newPath.push_back(neighbor);
                        queue.push(make_pair(neighbor, newPath));
                    }
                }
            }

            cout << "Não foi possível encontrar um caminho entre as estações " << startStation << " e " << endStation << endl;
        }
        else
        {
            cout << "Estação não encontrada!" << endl;
        }
    }

    void findShortestPath(const string &startStation, const string &endStation)
    {
        auto startIt = find_if(stations.begin(), stations.end(), [&](const Station &station)
                               { return station.name == startStation; });

        auto endIt = find_if(stations.begin(), stations.end(), [&](const Station &station)
                             { return station.name == endStation; });

        if (startIt != stations.end() && endIt != stations.end())
        {
            int startIndex = distance(stations.begin(), startIt);
            int endIndex = distance(stations.begin(), endIt);

            vector<int> distances(stations.size(), INT_MAX);
            vector<int> previous(stations.size(), -1);
            vector<bool> visited(stations.size(), false);
            priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;

            distances[startIndex] = 0;
            pq.push(make_pair(0, startIndex));

            while (!pq.empty())
            {
                int current = pq.top().second;
                pq.pop();

                if (current == endIndex)
                {
                    break;
                }

                if (visited[current])
                {
                    continue;
                }

                visited[current] = true;

                for (const auto &connection : adjacencyList[current])
                {
                    int neighbor = connection.first;
                    int weight = connection.second;

                    int newDistance = distances[current] + weight;
                    if (newDistance < distances[neighbor])
                    {
                        distances[neighbor] = newDistance;
                        previous[neighbor] = current;
                        pq.push(make_pair(newDistance, neighbor));
                    }
                }
            }

            if (distances[endIndex] != INT_MAX)
            {
                cout << "Menor caminho encontrado entre as estações " << startStation << " e " << endStation << ":" << endl;
                stack<int> pathStack;
                int current = endIndex;

                while (current != -1)
                {
                    pathStack.push(current);
                    current = previous[current];
                }

                while (!pathStack.empty())
                {
                    int stationIndex = pathStack.top();
                    pathStack.pop();
                    cout << stations[stationIndex].name << " ";
                }

                cout << endl;
                cout << "Tempo do caminho: " << distances[endIndex] << endl;
            }
            else
            {
                cout << "Não foi possível encontrar um caminho entre as estações " << startStation << " e " << endStation << endl;
            }
        }
        else
        {
            cout << "Estação não encontrada!" << endl;
        }
    }

    void findMinimumSpanningTree()
    {
        vector<bool> visited(stations.size(), false);
        vector<int> distances(stations.size(), INT_MAX);
        vector<int> parent(stations.size(), -1);

        distances[0] = 0;

        for (int i = 0; i < stations.size() - 1; i++)
        {
            int minDistance = INT_MAX;
            int minIndex = -1;

            for (int j = 0; j < stations.size(); j++)
            {
                if (!visited[j] && distances[j] < minDistance)
                {
                    minDistance = distances[j];
                    minIndex = j;
                }
            }

            if (minIndex != -1)
            {
                visited[minIndex] = true;

                for (const auto &connection : adjacencyList[minIndex])
                {
                    int neighbor = connection.first;
                    int weight = connection.second;

                    if (!visited[neighbor] && weight < distances[neighbor])
                    {
                        parent[neighbor] = minIndex;
                        distances[neighbor] = weight;
                    }
                }
            }
        }

        cout << "Árvore geradora mínima do sistema metroviário:" << endl;
        for (int i = 1; i < stations.size(); i++)
        {
            cout << stations[parent[i]].name << " - " << stations[i].name << endl;
        }
    }

    void printMetroSystem()
    {
        int choice;
        cout << "Escolha a forma de impressão do sistema metroviário:" << endl;
        cout << "1 - Lista de adjacência" << endl;
        cout << "2 - Matriz de adjacência" << endl;
        cout << "Opção: ";
        cin >> choice;

        switch (choice)
        {
        case 1:
            printAdjacencyList();
            break;
        case 2:
            printAdjacencyMatrix();
            break;
        default:
            cout << "Opção inválida!" << endl;
            break;
        }
    }

    void printAdjacencyList()
    {
        cout << "Lista de adjacência do sistema metroviário:" << endl;
        for (int i = 0; i < stations.size(); i++)
        {
            cout << stations[i].name << " -> ";
            for (const auto &connection : adjacencyList[i])
            {
                cout << stations[connection.first].name << "(" << connection.second << ") ";
            }
            cout << endl;
        }
    }

    void printAdjacencyMatrix()
    {
        cout << "Matriz de adjacência do sistema metroviário:" << endl;
        for (int i = 0; i < stations.size(); i++)
        {
            for (int j = 0; j < stations.size(); j++)
            {
                if (adjacencyMatrix[i][j] != -1)
                {
                    cout << adjacencyMatrix[i][j] << "\t";
                }
                else
                {
                    cout << "-\t";
                }
            }
            cout << endl;
        }
    }
};

int main()
{
    MetroSystem metroSystem;
    int option;

    do
    {
        cout << "Menu de Controle do Sistema Metroviário" << endl;
        cout << "1 - Criar o grafo" << endl;
        cout << "2 - Adicionar estacao" << endl;
        cout << "3 - Remover estacao" << endl;
        cout << "4 - Busca por uma estacao (largura)" << endl;
        cout << "5 - Encontrar um caminho entre estacoes" << endl;
        cout << "6 - Encontrar o menor caminho entre estacoes" << endl;
        cout << "7 - Encontrar o mínimo de arestas do sistema metroviário" << endl;
        cout << "8 - Imprimir o sistema metroviário" << endl;
        cout << "0 - Sair" << endl;
        cout << "Escolha uma opção: ";
        cin >> option;

        switch (option)
        {
        case 1:
            metroSystem.createGraph();
            break;
        case 2:
            metroSystem.addStation();
            break;
        case 3:
            metroSystem.removeStation();
            break;
        case 4:
        {
            string startStation;
            cout << "Digite o nome da estação inicial: ";
            cin >> startStation;
            metroSystem.breadthFirstSearch(startStation);
            break;
        }
        case 5:
        {
            string startStation, endStation;
            cout << "Digite o nome da estação de partida: ";
            cin >> startStation;
            cout << "Digite o nome da estação de destino: ";
            cin >> endStation;
            metroSystem.findPath(startStation, endStation);
            break;
        }
        case 6:
        {
            string startStation, endStation;
            cout << "Digite o nome da estação de partida: ";
            cin >> startStation;
            cout << "Digite o nome da estação de destino: ";
            cin >> endStation;
            metroSystem.findShortestPath(startStation, endStation);
            break;
        }
        case 7:
            metroSystem.findMinimumSpanningTree();
            break;
        case 8:
            metroSystem.printMetroSystem();
            break;
        case 0:
            cout << "Saindo do programa..." << endl;
            break;
        default:
            cout << "Opção inválida!" << endl;
            break;
        }

        cout << endl;
    } while (option != 0);

    return 0;
}
