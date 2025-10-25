import React from 'react'
import { render, screen } from '@testing-library/react'
import { ProductCard } from '../src/components/ProductCard'

describe('ProductCard Component', () => {
  const mockProduct = {
    id: 1,
    name: 'Laptop',
    description: 'High-performance laptop',
    price: 999.99,
    in_stock: true,
  }

  test('renders product information', () => {
    render(<ProductCard product={mockProduct} />)

    expect(screen.getByText('Laptop')).toBeInTheDocument()
    expect(screen.getByText('High-performance laptop')).toBeInTheDocument()
  })

  test('displays price correctly', () => {
    render(<ProductCard product={mockProduct} />)

    expect(screen.getByText('$999.99')).toBeInTheDocument()
  })

  test('displays in stock status', () => {
    render(<ProductCard product={mockProduct} />)

    expect(screen.getByText('In Stock')).toBeInTheDocument()
  })

  test('displays out of stock status when product is not in stock', () => {
    const outOfStockProduct = { ...mockProduct, in_stock: false }

    render(<ProductCard product={outOfStockProduct} />)

    expect(screen.getByText('Out of Stock')).toBeInTheDocument()
  })
})
