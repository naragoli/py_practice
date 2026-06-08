import React, { useState } from 'react';
import { View, TextInput, TouchableOpacity, Text, StyleSheet } from 'react-native';

export default function AddTask({ onAdd }) {
  const [text, setText] = useState('');

  const submit = () => {
    if (!text.trim()) return;
    onAdd(text);
    setText('');
  };

  return (
    <View style={styles.row}>
      <TextInput
        value={text}
        onChangeText={setText}
        placeholder="Add a new task"
        style={styles.input}
        onSubmitEditing={submit}
        returnKeyType="done"
      />
      <TouchableOpacity style={styles.addBtn} onPress={submit}>
        <Text style={styles.addBtnText}>Add</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  row: { flexDirection: 'row', padding: 12, alignItems: 'center' },
  input: { flex: 1, backgroundColor: 'white', padding: 10, borderRadius: 6, marginRight: 8 },
  addBtn: { backgroundColor: '#10b981', paddingVertical: 10, paddingHorizontal: 14, borderRadius: 6 },
  addBtnText: { color: 'white', fontWeight: '600' },
});
