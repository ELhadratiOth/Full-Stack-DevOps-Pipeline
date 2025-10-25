import React, { useEffect, useState } from 'react'
import { productsApi } from '../services/api'
import { ProductCard } from '../components/ProductCard'
import { Product } from '../types'

export default function Products() {
  const [products, setProducts] = useState<Product[]>([])
  const [loading, setLoading] = useState(true)
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const fetchProducts = async () => {
      try {
        const data = await productsApi.list()
        setProducts(data)
        setError(null)
      } catch (err) {
        setError('Failed to load products')
        setProducts([])
      } finally {
        setLoading(false)
      }
    }

    fetchProducts()
  }, [])

  return (
    <div className="min-h-screen bg-gray-50">
      <header className="bg-white shadow">
        <div className="max-w-7xl mx-auto py-6 px-4">
          <h1 className="text-3xl font-bold text-gray-900">Products</h1>
        </div>
      </header>

      <main className="max-w-7xl mx-auto py-12 px-4">
        {loading && <p className="text-center text-gray-600">Loading products...</p>}

        {error && <div className="bg-red-50 border border-red-200 rounded p-4 text-red-700 mb-4">{error}</div>}

        {!loading && products.length > 0 && (
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {products.map((product) => (
              <ProductCard key={product.id} product={product} />
            ))}
          </div>
        )}

        {!loading && products.length === 0 && !error && <p className="text-center text-gray-600">No products found</p>}

        <a href="/" className="inline-block mt-8 text-blue-600 hover:underline">
          Back to Home
        </a>
      </main>
    </div>
  )
}
