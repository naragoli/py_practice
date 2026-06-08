import React, { useState, useEffect } from 'react';
import { SafeAreaView, View, FlatList, Text, StyleSheet, Alert } from 'react-native';
import AsyncStorage from '@react-native-async-storage/async-storage';
import AddTask from './components/AddTask';
import TaskItem from './components/TaskItem';

const STORAGE_KEY = '@tasks_v1';

export default function App() {
  const [tasks, setTasks] = useState([]);

  useEffect(() => {
    loadTasks();
  }, []);

  useEffect(() => {
    saveTasks(tasks);
  }, [tasks]);

  const loadTasks = async () => {
    try {
      const raw = await AsyncStorage.getItem(STORAGE_KEY);
      if (raw) setTasks(JSON.parse(raw));
    } catch (e) {
      Alert.alert('Error', 'Failed to load tasks');
    }
  };

  const saveTasks = async (list) => {
    try {
      await AsyncStorage.setItem(STORAGE_KEY, JSON.stringify(list));
    } catch (e) {
      Alert.alert('Error', 'Failed to save tasks');
    }
  };

  const addTask = (text) => {
    if (!text || !text.trim()) return;
    const newTask = { id: Date.now().toString(), text: text.trim(), done: false };
    setTasks((s) => [newTask, ...s]);
  };

  const toggleTask = (id) => {
    setTasks((s) => s.map(t => t.id === id ? { ...t, done: !t.done } : t));
  };

  const deleteTask = (id) => {
    setTasks((s) => s.filter(t => t.id !== id));
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Simple Todo (Android)</Text>
      </View>

      <AddTask onAdd={addTask} />

      <FlatList
        data={tasks}
        keyExtractor={(item) => item.id}
        contentContainerStyle={{ padding: 16 }}
        renderItem={({ item }) => (
          <TaskItem
            task={item}
            onToggle={() => toggleTask(item.id)}
            onDelete={() => deleteTask(item.id)}
          />
        )}
        ListEmptyComponent={<Text style={styles.empty}>No tasks — add one.</Text>}
      />
    </SafeAreaView>
  );
}

const styles = StyleSheet.create({
  container: { flex: 1, backgroundColor: '#f3f4f6' },
  header: { padding: 16, backgroundColor: '#2563eb' },
  title: { color: 'white', fontSize: 20, fontWeight: '600' },
  empty: { textAlign: 'center', marginTop: 24, color: '#6b7280' },
});
