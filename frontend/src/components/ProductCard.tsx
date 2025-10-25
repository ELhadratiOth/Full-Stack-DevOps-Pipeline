import React from 'react'
import { Product } from '../types'

interface ProductCardProps {
  product: Product
}

export const ProductCard: React.FC<ProductCardProps> = ({ product }) => {
  return (
    <div className="p-4 border border-gray-200 rounded-lg shadow-sm hover:shadow-md transition">
      <h3 className="text-lg font-semibold text-gray-900">{product.name}</h3>
      <p className="text-sm text-gray-600">{product.description}</p>
      <div className="mt-4 flex justify-between items-center">
        <span className="text-xl font-bold text-gray-900">${product.price}</span>
        <span className={`px-2 py-1 rounded text-xs ${product.in_stock ? 'bg-blue-100 text-blue-800' : 'bg-gray-100 text-gray-800'}`}>
          {product.in_stock ? 'In Stock' : 'Out of Stock'}
        </span>
      </div>
    </div>
  )
}
