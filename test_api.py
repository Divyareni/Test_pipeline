import pytest
import cpp_api
import os

@pytest.mark.parametrize("val, expected", [(2, 4), (10, 100)])
def test_performance_and_logic(val, expected):
    start_time = time.perf_counter()
    
    result = cpp_api.compute(val)
    
    end_time = time.perf_counter()
    duration = end_time - start_time
    
    # 1. Logic Check
    assert result == expected
    
    # 2. Runtime Profiling Check (The "Standard" you set)
    print(f"\nRuntime: {duration:.6f}s")
    assert duration < 0.001, "Performance regression detected!"
