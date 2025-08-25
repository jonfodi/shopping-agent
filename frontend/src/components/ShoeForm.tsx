import { useState } from "react";
import { Button } from "@/components/ui/button";
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card";
import { Input } from "@/components/ui/input";
import { Label } from "@/components/ui/label";
import { Select, SelectContent, SelectItem, SelectTrigger, SelectValue } from "@/components/ui/select";
import { ScrollArea } from "@/components/ui/scroll-area";
import { Loader2, Search } from "lucide-react";

interface ShoeFormProps {
  onSubmit: (data: ShoeFormData) => void;
  isLoading: boolean;
}

export interface ShoeFormData {
  shoe_type: string;
  size: number;
  budget: number;
  color: string;
  gender: string;
}

const shoeTypes = [
  { value: "air force one", label: "Air Force One" },
  { value: "air jordan", label: "Air Jordan" },
  { value: "air max", label: "Air Max" },
  { value: "running", label: "Running" },
  { value: "training", label: "Training" },
  { value: "basketball", label: "Basketball" },
  { value: "football", label: "Football" },
  { value: "tennis", label: "Tennis" },
  { value: "golf", label: "Golf" },
];

const genders = [
  { value: "men", label: "Men" },
  { value: "women", label: "Women" },
];

const sizes = Array.from({ length: 12 }, (_, i) => i + 4); // 4 to 15

export function ShoeForm({ onSubmit, isLoading }: ShoeFormProps) {
  const [formData, setFormData] = useState<ShoeFormData>({
    shoe_type: "",
    size: 10,
    budget: 100,
    color: "",
    gender: "",
  });

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(formData);
  };

  const isFormValid = formData.shoe_type && formData.gender && formData.color;

  return (
    <Card className="w-full max-w-2xl mx-auto shadow-card hover:shadow-hover transition-all duration-300">
      <CardHeader className="text-center space-y-2">
        <CardTitle className="text-3xl font-bold bg-gradient-nike bg-clip-text text-transparent">
          Nike Shoe Finder
        </CardTitle>
        <CardDescription className="text-lg text-muted-foreground">
          Find your perfect Nike shoes with our intelligent shopping agent
        </CardDescription>
      </CardHeader>
      <CardContent>
        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
            <div className="space-y-2">
              <Label htmlFor="shoe-type" className="text-sm font-semibold">
                Shoe Type
              </Label>
              <Select
                value={formData.shoe_type}
                onValueChange={(value) => setFormData({ ...formData, shoe_type: value })}
              >
                <SelectTrigger className="h-12 border-2 focus:border-accent">
                  <SelectValue placeholder="Select shoe type" />
                </SelectTrigger>
                <SelectContent className="bg-popover border-2">
                  {shoeTypes.map((type) => (
                    <SelectItem key={type.value} value={type.value}>
                      {type.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="gender" className="text-sm font-semibold">
                Gender
              </Label>
              <Select
                value={formData.gender}
                onValueChange={(value) => setFormData({ ...formData, gender: value })}
              >
                <SelectTrigger className="h-12 border-2 focus:border-accent">
                  <SelectValue placeholder="Select gender" />
                </SelectTrigger>
                <SelectContent className="bg-popover border-2">
                  {genders.map((gender) => (
                    <SelectItem key={gender.value} value={gender.value}>
                      {gender.label}
                    </SelectItem>
                  ))}
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="size" className="text-sm font-semibold">
                Size (US)
              </Label>
              <Select
                value={formData.size.toString()}
                onValueChange={(value) => setFormData({ ...formData, size: Number(value) })}
              >
                <SelectTrigger className="h-12 border-2 focus:border-accent">
                  <SelectValue />
                </SelectTrigger>
                <SelectContent className="bg-popover border-2">
                  <ScrollArea className="h-48">
                    {sizes.map((size) => (
                      <SelectItem key={size} value={size.toString()}>
                        US {size}
                      </SelectItem>
                    ))}
                  </ScrollArea>
                </SelectContent>
              </Select>
            </div>

            <div className="space-y-2">
              <Label htmlFor="budget" className="text-sm font-semibold">
                Budget ($)
              </Label>
              <Input
                id="budget"
                type="number"
                min="50"
                max="1000"
                value={formData.budget}
                onChange={(e) => setFormData({ ...formData, budget: Number(e.target.value) })}
                className="h-12 border-2 focus:border-accent"
              />
            </div>
          </div>

          <div className="space-y-2">
            <Label htmlFor="color" className="text-sm font-semibold">
              Preferred Color
            </Label>
            <Input
              id="color"
              type="text"
              placeholder="e.g., red, black, white"
              value={formData.color}
              onChange={(e) => setFormData({ ...formData, color: e.target.value })}
              className="h-12 border-2 focus:border-accent"
            />
          </div>

          <Button
            type="submit"
            disabled={!isFormValid || isLoading}
            className="w-full h-12 bg-gradient-nike hover:shadow-nike text-white font-semibold text-lg transition-all duration-300 disabled:opacity-50"
          >
            {isLoading ? (
              <>
                <Loader2 className="mr-2 h-5 w-5 animate-spin" />
                Finding Shoes...
              </>
            ) : (
              <>
                <Search className="mr-2 h-5 w-5" />
                Find My Shoes
              </>
            )}
          </Button>
        </form>
      </CardContent>
    </Card>
  );
}