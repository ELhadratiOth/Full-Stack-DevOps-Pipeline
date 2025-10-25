import axios from 'axios'
import { User, Product, ApiResponse } from '../types'

const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000'

const apiClient = axios.create({
  baseURL: API_URL,
  headers: {
    'Content-Type': 'application/json',
  },
})

// Users API
export const usersApi = {
  list: async (): Promise<User[]> => {
    const response = await apiClient.get('/api/v1/users/')
    return response.data
  },
  get: async (id: number): Promise<User> => {
    const response = await apiClient.get(`/api/v1/users/${id}`)
    return response.data
  },
  create: async (user: Omit<User, 'id'>): Promise<User> => {
    const response = await apiClient.post('/api/v1/users/', user)
    return response.data
  },
  update: async (id: number, user: Omit<User, 'id'>): Promise<User> => {
    const response = await apiClient.put(`/api/v1/users/${id}`, user)
    return response.data
  },
  delete: async (id: number): Promise<void> => {
    await apiClient.delete(`/api/v1/users/${id}`)
  },
}

// Products API
export const productsApi = {
  list: async (): Promise<Product[]> => {
    const response = await apiClient.get('/api/v1/products/')
    return response.data
  },
  get: async (id: number): Promise<Product> => {
    const response = await apiClient.get(`/api/v1/products/${id}`)
    return response.data
  },
  create: async (product: Omit<Product, 'id'>): Promise<Product> => {
    const response = await apiClient.post('/api/v1/products/', product)
    return response.data
  },
  update: async (id: number, product: Omit<Product, 'id'>): Promise<Product> => {
    const response = await apiClient.put(`/api/v1/products/${id}`, product)
    return response.data
  },
  delete: async (id: number): Promise<void> => {
    await apiClient.delete(`/api/v1/products/${id}`)
  },
}

// Health API
export const healthApi = {
  check: async (): Promise<ApiResponse<any>> => {
    const response = await apiClient.get('/health')
    return response.data
  },
  ready: async (): Promise<ApiResponse<any>> => {
    const response = await apiClient.get('/readiness')
    return response.data
  },
}
