var (
    todos   []TodoItem
    nextID  int
    todosMu sync.Mutex
)

// getAllTodos はすべてのTo-Doアイテムを返します。
func getAllTodos(w http.ResponseWriter, r *http.Request) {
    todosMu.Lock()
    defer todosMu.Unlock()

    json.NewEncoder(w).Encode(todos)
}

// addTodo は新しいTo-Doアイテムを追加します。
func addTodo(w http.ResponseWriter, r *http.Request) {
    todosMu.Lock()
    defer todosMu.Unlock()

    var todo TodoItem
    if err := json.NewDecoder(r.Body).Decode(&todo); err != nil {
        http.Error(w, err.Error(), http.StatusBadRequest)
        return
    }

    todo.ID = nextID
    nextID++
    todos = append(todos, todo)

    json.NewEncoder(w).Encode(todo)
}

// deleteTodo は指定されたIDのTo-Doアイテムを削除します。
func deleteTodo(w http.ResponseWriter, r *http.Request) {
    todosMu.Lock()
    defer todosMu.Unlock()

    vars := mux.Vars(r)
    id, err := strconv.Atoi(vars["id"])
    if err != nil {
        http.Error(w, "Invalid todo ID", http.StatusBadRequest)
        return
    }

    for i, todo := range todos {
        if todo.ID == id {
            todos = append(todos[:i], todos[i+1:]...)
            fmt.Fprintf(w, "Deleted todo %d", id)
            return
        }
    }

    http.NotFound(w, r)
}
