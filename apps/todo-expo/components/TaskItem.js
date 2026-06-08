import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet } from 'react-native';

export default function TaskItem({ task, onToggle, onDelete }) {
  return (
    <View style={styles.row}>
      <TouchableOpacity onPress={onToggle} style={[styles.check, task.done && styles.checked]}>
        {task.done ? <Text style={styles.checkText}>✓</Text> : null}
      </TouchableOpacity>

      <Text style={[styles.text, task.done && styles.doneText]} numberOfLines={1}>{task.text}</Text>

      <TouchableOpacity onPress={onDelete} style={styles.delBtn}>
        <Text style={styles.delText}>Del</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  row: { flexDirection: 'row', alignItems: 'center', paddingVertical: 8 },
  check: { width: 28, height: 28, borderRadius: 6, borderWidth: 1, borderColor: '#9ca3af', alignItems: 'center', justifyContent: 'center', marginRight: 12, backgroundColor: 'white' },
  checked: { backgroundColor: '#34d399', borderColor: '#34d399' },
  checkText: { color: 'white', fontWeight: '700' },
  text: { flex: 1, fontSize: 16, color: '#111827' },
  doneText: { textDecorationLine: 'line-through', color: '#6b7280' },
  delBtn: { paddingHorizontal: 10, paddingVertical: 6 },
  delText: { color: '#ef4444', fontWeight: '600' },
});
